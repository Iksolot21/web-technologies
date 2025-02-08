import os
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        files_by_extension = {}
        
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                name, ext = os.path.splitext(filename)
                if ext not in files_by_extension:
                    files_by_extension[ext] = []
                files_by_extension[ext].append(filename)

        sorted_extensions = sorted(files_by_extension.keys())
        
        for ext in sorted_extensions:
            sorted_files = sorted(files_by_extension[ext])
            for filename in sorted_files:
                print(filename)
    else:
        print("Не указан путь к директории.")