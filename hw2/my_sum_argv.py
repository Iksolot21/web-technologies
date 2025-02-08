import sys

if __name__ == '__main__':
    numbers = [float(arg) for arg in sys.argv[1:]]
    result = sum(numbers)
    print(result)