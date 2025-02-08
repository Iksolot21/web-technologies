import os
import sys

def find_file(filename, start_dir):
    for root, _, files in os.walk(start_dir):
        if filename in files:
            return os.path.join(root, filename)
    return None

def print_file_head(filepath, num_lines=5):
    try:
        with open(filepath, 'r') as f:
            for i in range(num_lines):
                print(f.readline(), end='')
    except FileNotFoundError:
        print(f"Файл {filepath} не найден")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        start_dir = os.getcwd()
        
        filepath = find_file(filename, start_dir)
        
        if filepath:
            print_file_head(filepath)
        else:
            print(f"Файл {filename} не найден")
    else:
        print("Не указано имя файла.")