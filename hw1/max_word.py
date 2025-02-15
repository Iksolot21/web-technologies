import re

def find_max_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text)  

    if not words:
        return []

    max_len = max(len(word) for word in words) 
    max_words = sorted(word for word in words if len(word) == max_len) 
    return max_words

if __name__ == "__main__":
    max_words = find_max_words("example.txt")
    print("\n".join(max_words)) 
