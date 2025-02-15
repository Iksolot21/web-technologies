import random
from flask import Flask, render_template, url_for, request
from faker import Faker
import os
from datetime import datetime

fake = Faker()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  

class Post:
    def __init__(self, title, author, date, image_id, text):
        self.title = title
        self.author = author
        self.date = date
        self.image_id = image_id
        self.text = text

class Comment:
    def __init__(self, author, text, avatar="avatar.jpg", replies=None):
        self.author = author
        self.text = text
        self.avatar = avatar  
        self.replies = replies or []

images_ids = ['7d4e9175-95ea-4c5f-8be5-92a6b708bb3c',
              '2d2ab7df-cdbc-48a8-a936-35bba702def5',
              '6e12f3de-d5fd-4ebb-855b-8cbc485278b7',
              'afc2cfe7-5cac-4b80-9b9a-d5c65ef0c728',
              'cab5b7f2-774e-4884-a200-0c0180fa777f']

def generate_comments(replies=True, max_level=2):  
    comments = []
    for i in range(random.randint(1, 3)):  
        comment = {
            'author': fake.name(),
            'text': fake.text(),
            'avatar': 'avatar.jpg'
        }
        if replies and max_level > 0:  
            comment['replies'] = generate_comments(replies=True, max_level=max_level - 1)  
        else:
            comment['replies'] = [] 
        comments.append(comment)
    return comments

def generate_post(i):
    return {
        'title': 'Заголовок поста',
        'text': fake.paragraph(nb_sentences=100),
        'author': fake.name(),
        'date': fake.date_time_between(start_date='-2y', end_date='now'),
        'image_id': f'{images_ids[i]}.jpg',
        'comments': generate_comments()
    }

posts_list = sorted([generate_post(i) for i in range(5)], key=lambda p: p['date'], reverse=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', title='Посты', posts=posts_list)



@app.route('/posts/<int:index>', methods=['GET', 'POST'])
def post(index):
    p = posts_list[index]
    comments = p['comments']

    if request.method == 'POST':
        comment_text = request.form.get('comment')
        if comment_text:
            new_comment = Comment(author="Аноним", text=comment_text, avatar="avatar.jpg")
            comments.append(new_comment.__dict__) 

    return render_template('post.html', title=p['title'], post=p, comments=comments)

@app.route('/about')
def about():
    return render_template('about.html', title='Об авторе')

def display_comments(comments, level=0):
    result = ''
    for comment in comments:
        result += f'''
            <div class="media mt-{(4 + level * 2)} comment-level-{level}">
                <img class="d-flex mr-3 rounded-circle avatar" src="{url_for('static', filename='images/' + comment['avatar'])}" alt="Generic placeholder image">
                <div class="media-body">
                    <h5 class="mt-0">{comment['author']}</h5>
                    {comment['text']}
                    '''
        if comment['replies']:
            result += display_comments(comment['replies'], level + 1)
        result += f'''
                    <button class="btn btn-sm btn-secondary mt-2">Ответить</button>
                </div>
            </div>
            '''
    return result

if __name__ == '__main__':
    app.run(debug=True)