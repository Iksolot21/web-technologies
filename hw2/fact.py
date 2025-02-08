import timeit

def fact_rec(n):
    if n == 0:
        return 1
    else:
        return n * fact_rec(n-1)

def fact_it(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    n = 10
    
    # Сравнение скорости
    time_rec = timeit.timeit(lambda: fact_rec(n), number=10000)
    time_it = timeit.timeit(lambda: fact_it(n), number=10000)
    
    print(f"Рекурсивная функция: {time_rec}")
    print(f"Итеративная функция: {time_it}")
    # Итеративная функция работает быстрее, чем рекурсивная.