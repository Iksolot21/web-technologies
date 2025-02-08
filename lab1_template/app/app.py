import random
from flask import Flask, render_template, url_for, request, make_response
from faker import Faker
import os
import re
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
            'avatar': 'avatar.jpg',
            'replies': []  # Initialize replies here
        }
        if replies and max_level > 0:
            comment['replies'] = generate_comments(replies=True, max_level=max_level - 1)
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

@app.route('/request_data')
def request_data():
    """Отображает данные запроса."""
    url_params = request.args.to_dict()
    headers = dict(request.headers)
    cookies = request.cookies
    form_params = request.form.to_dict()  # Initially empty until there's a form
    return render_template('request_data.html',
                           title='Данные запроса',
                           url_params=url_params,
                           headers=headers,
                           cookies=cookies,
                           form_params=form_params)

@app.route('/phone_form', methods=['GET', 'POST'])
def phone_form():
    """Страница с формой для ввода номера телефона и его проверки."""
    error_message = None
    formatted_number = None
    phone_number = None  # Initialize phone_number

    if request.method == 'POST':
        phone_number = request.form.get('phone')
        if phone_number:
            # Remove all characters except digits
            digits_only = re.sub(r'\D', '', phone_number)
            number_length = len(digits_only)

            if number_length not in (10, 11):
                error_message = "Недопустимый ввод. Неверное количество цифр."
            elif not re.match(r'^[\d\s()+.-]+$', phone_number):
                error_message = "Недопустимый ввод. В номере телефона встречаются недопустимые символы."
            else:
                # Convert to 8-***-***-**-** format
                if number_length == 11:
                    if digits_only.startswith('7') or digits_only.startswith('8'):
                        formatted_number = f"8-{digits_only[1:4]}-{digits_only[4:7]}-{digits_only[7:9]}-{digits_only[9:11]}"
                    else:
                        error_message = "Недопустимый ввод. Неверный формат номера телефона (11 цифр)."
                else:
                    formatted_number = f"8-{digits_only[0:3]}-{digits_only[3:6]}-{digits_only[6:8]}-{digits_only[8:10]}"
        else:
            error_message = "Пожалуйста, введите номер телефона."

    return render_template('phone_form.html',
                           title='Форма телефона',
                           error_message=error_message,
                           formatted_number=formatted_number,
                           phone_number=phone_number)

# Cookie example
@app.route('/set_cookie')
def set_cookie():
    """Sets a cookie."""
    response = make_response(render_template('set_cookie.html', title='Установка Cookie'))
    response.set_cookie('my_cookie', 'cookie_value')
    return response

if __name__ == '__main__':
    app.run(debug=True)