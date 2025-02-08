import random
import math

def circle_square_mk(r, n):
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if x**2 + y**2 <= r**2:
            inside_circle += 1
    return 4 * r**2 * (inside_circle / n)

if __name__ == '__main__':
    r = 1
    n = 100000
    approx_area = circle_square_mk(r, n)
    exact_area = math.pi * r**2
    
    print(f"Приблизительная площадь: {approx_area}")
    print(f"Точная площадь: {exact_area}")
    print(f"Погрешность: {abs(approx_area - exact_area)}")
    # Погрешность уменьшается с увеличением количества экспериментов (n).