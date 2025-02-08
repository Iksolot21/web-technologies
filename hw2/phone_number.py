def wrapper(f):
    def fun(l):
        formatted_numbers = []
        for number in l:
            number = number[-10:]  # Берем последние 10 цифр
            formatted_numbers.append("+7 (" + number[:3] + ") " + number[3:6] + "-" + number[6:8] + "-" + number[8:])
        return formatted_numbers
    return fun

@wrapper
def sort_phone(l):
    return sorted(l)

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    print(*sort_phone(l), sep='\n')