import timeit

def process_list(arr):
    result = []
    for i in arr:
        if i % 2 == 0:
            result.append(i**2)
        else:
            result.append(i**3)
    return result

def process_list_comprehension(arr):
    return [i**2 if i % 2 == 0 else i**3 for i in arr]

def process_list_gen(arr):
    for i in arr:
        if i % 2 == 0:
            yield i**2
        else:
            yield i**3

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    
    num = 10000
    time_original = timeit.timeit(lambda: process_list(arr), number=num)
    time_comprehension = timeit.timeit(lambda: process_list_comprehension(arr), number=num)
    time_generator = timeit.timeit(lambda: list(process_list_gen(arr)), number=num) 
    
    print(f"Исходная функция: {time_original}")
    print(f"List comprehension: {time_comprehension}")
    print(f"Функция-генератор: {time_generator}")