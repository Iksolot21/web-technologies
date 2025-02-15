import subprocess
import pytest
import math
import os
import re
import tempfile

INTERPRETER = 'python3'

def run_script(filename, input_data=None):
    if input_data:
        command = INTERPRETER + " " + filename + " " + ' '.join(input_data)
    else:
        command = INTERPRETER + " " + filename
    proc = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=False,
        shell=True 
    )
    return proc.stdout.strip()

# ==================== Функции для тестирования ====================

# fact.py
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

# show_employee.py
def show_employee(name, salary=100000):
    return f"{name}: {salary} $"

# sum_and_sub.py
def sum_and_sub(a, b):
    return a + b, a - b

# process_list.py
def process_list(lst):
    result = []
    for x in lst:
        if x % 2 == 0:
            result.append(x**2)
        else:
            result.append(x**3)
    return result

def process_list_comprehension(lst):
    return [x**2 if x % 2 == 0 else x**3 for x in lst]

def process_list_gen(lst):
    for x in lst:
        if x % 2 == 0:
            yield x**2
        else:
            yield x**3

# my_sum.py
def my_sum(*args):
    return sum(args)

# email_validation.py
def fun(s):
    pattern = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    return bool(re.match(pattern, s))

def filter_mail(emails):
    return list(filter(fun, emails))

# fibonacci.py
def fibonacci(n):
    list_fib = [0, 1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    while len(list_fib) < n:
        next_fib = list_fib[-1] + list_fib[-2]
        list_fib.append(next_fib)
    return list_fib[:n]

def cube(x):
    return x**3

# average_scores.py
def compute_average_scores(scores):
    num_students = len(scores)
    num_subjects = len(scores[0]) if num_students > 0 else 0
    average_scores = []

    for j in range(num_subjects):
        total_score = sum(scores[i][j] for i in range(num_students))
        average_scores.append(total_score / num_students)

    return tuple(average_scores)

# plane_angle.py
class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        x = self.x - no.x
        y = self.y - no.y
        z = self.z - no.z
        return (x, y, z)

    def dot(self, no):
        x = self.x * no.x
        y = self.y * no.y
        z = self.z * no.z
        return x + y + z

    def cross(self, no):
        x = self.y * no.z - self.z * no.y
        y = self.z * no.x - self.x * no.z
        z = self.x * no.y - self.y * no.x
        return (x, y, z)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

def plane_angle(a, b, c, d):
    vector_1 = (b.x - a.x, b.y - a.y, b.z - a.z)
    vector_2 = (c.x - b.x, c.y - b.y, c.z - b.z)
    vector_3 = (d.x - c.x, d.y - c.y, d.z - c.z)

    normal_1 = (vector_1[1] * vector_2[2] - vector_1[2] * vector_2[1],
                vector_1[2] * vector_2[0] - vector_1[0] * vector_2[2],
                vector_1[0] * vector_2[1] - vector_1[1] * vector_2[0])

    normal_2 = (vector_2[1] * vector_3[2] - vector_2[2] * vector_3[1],
                vector_2[2] * vector_3[0] - vector_2[0] * vector_3[2],
                vector_2[0] * vector_3[1] - vector_2[1] * vector_3[0])
    dot_product = sum(n1 * n2 for n1, n2 in zip(normal_1, normal_2))

    magnitude_1 = math.sqrt(sum(n1 ** 2 for n1 in normal_1))
    magnitude_2 = math.sqrt(sum(n2 ** 2 for n2 in normal_2))

    if magnitude_1 == 0 or magnitude_2 == 0:
        return 0.0

    angle = math.acos(dot_product / (magnitude_1 * magnitude_2))
    angle_degrees = math.degrees(angle)

    return angle_degrees

# phone_number.py
def sort_phone(phone):
    def wrapper(phone):
        output = []
        for x in phone:
            x = "".join(filter(str.isdigit, x))
            if len(x) == 10:
                output.append("+7 ("+ x[:3] +") "+ x[3:6] +"-"+ x[6:8] +"-"+ x[8:])
            elif len(x) == 11:
                output.append("+7 ("+ x[1:4] +") "+ x[4:7] +"-"+ x[7:9] +"-"+ x[9:])

        return output
    return wrapper(phone)

def wrapper(f):  
    def fun(l):
        return f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
    return fun

# people_sort.py
def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

# complex_numbers.py
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def __truediv__(self, no):
        denominator = no.real ** 2 + no.imaginary ** 2
        real = (self.real * no.real + self.imaginary * no.imaginary) / denominator
        imaginary = (self.imaginary * no.real - self.real * no.imaginary) / denominator
        return Complex(real, imaginary)

    def mod(self):
        modulus = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(modulus, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

# circle_square_mk.py
def circle_square_mk(r, n):
    import random
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for i in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)

        if x**2 + y**2 <= r**2:
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)
    area = (len(x_inside) * ((2*r)**2)) / n
    return area

def file_sort(directory):
    files_by_extension = {}
    output = []

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath): 
            if not filename.startswith('.'):  
                name, ext = os.path.splitext(filename)
                if ext not in files_by_extension:
                    files_by_extension[ext] = []
                files_by_extension[ext].append(filename)

    sorted_extensions = sorted(files_by_extension.keys())

    for ext in sorted_extensions:
        sorted_files = sorted(files_by_extension[ext])
        output.extend(sorted_files)

    return '\n'.join(output)

def file_search(directory, filename):  
    filepath = os.path.join(directory, filename) 
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            return "".join(lines[:5]).strip()  
    except FileNotFoundError:
        return f"Файл {filename} не найден"  

# ==================== Тесты ====================
# fact.py tests
def test_fact_rec_positive():
    assert fact_rec(5) == 120
def test_fact_rec_zero():
    assert fact_rec(0) == 1
def test_fact_rec_one():
    assert fact_rec(1) == 1
def test_fact_it_positive():
    assert fact_it(5) == 120
def test_fact_it_zero():
    assert fact_it(0) == 1
def test_fact_it_one():
    assert fact_it(1) == 1

# show_employee.py tests
def test_show_employee_default_salary():
    assert show_employee("Alice") == "Alice: 100000 $"
def test_show_employee_custom_salary():
    assert show_employee("Bob", 50000) == "Bob: 50000 $"
def test_show_employee_empty_name():
    assert show_employee("") == ": 100000 $"
def test_show_employee_zero_salary():
    assert show_employee("Charlie", 0) == "Charlie: 0 $"

# sum_and_sub.py tests
def test_sum_and_sub_positive():
    assert sum_and_sub(5, 3) == (8, 2)
def test_sum_and_sub_negative():
    assert sum_and_sub(-5, 3) == (-2, -8)
def test_sum_and_sub_zero():
    assert sum_and_sub(0, 0) == (0, 0)
def test_sum_and_sub_float():
    assert sum_and_sub(2.5, 1.5) == (4.0, 1.0)

# process_list.py tests
def test_process_list_even_odd():
    assert process_list([1, 2, 3, 4]) == [1, 4, 27, 16]
def test_process_list_comprehension_even_odd():
    assert process_list_comprehension([1, 2, 3, 4]) == [1, 4, 27, 16]
def test_process_list_gen_even_odd():
    assert list(process_list_gen([1, 2, 3, 4])) == [1, 4, 27, 16]
def test_process_list_empty():
    assert process_list([]) == []
def test_process_list_comprehension_empty():
    assert process_list_comprehension([]) == []
def test_process_list_gen_empty():
    assert list(process_list_gen([])) == []

# my_sum.py tests
def test_my_sum_empty():
    assert my_sum() == 0
def test_my_sum_single():
    assert my_sum(5) == 5
def test_my_sum_multiple():
    assert my_sum(1, 2, 3, 4) == 10
def test_my_sum_negative():
    assert my_sum(-1, -2, -3) == -6
def test_my_sum_float():
    assert my_sum(1.5, 2.5, 3.5) == 7.5

# email_validation.py tests
def test_email_validation_valid():
    assert fun("test@example.com") == True
def test_email_validation_invalid_format():
    assert fun("testexample.com") == False
def test_email_validation_invalid_chars():
    assert fun("test!@example.com") == False
def test_email_validation_long_extension():
    assert fun("test@example.long") == False
def test_email_validation_filter_mail():
    emails = ["test@example.com", "invalid", "valid@test.net"]
    assert filter_mail(emails) == ["test@example.com", "valid@test.net"]
def test_email_validation_filter_mail_empty():
    emails = []
    assert filter_mail(emails) == []

# fibonacci.py tests
def test_fibonacci_empty():
    assert fibonacci(0) == []
def test_fibonacci_single():
    assert fibonacci(1) == [0]
def test_fibonacci_multiple():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
def test_cube_positive():
    assert cube(3) == 27
def test_cube_negative():
    assert cube(-2) == -8
def test_fibonacci_cube_integration():
    assert list(map(cube, fibonacci(5))) == [0, 1, 1, 8, 27]

# average_scores.py tests
def test_average_scores_simple():
    scores = [(80, 90, 70), (90, 80, 60)]
    assert compute_average_scores(scores) == (85.0, 85.0, 65.0)
def test_average_scores_uneven():
    scores = [(80, 90), (90, 80)]
    assert compute_average_scores(scores) == (85.0, 85.0)
def test_average_scores_single():
    scores = [(80,), (90,)]
    assert compute_average_scores(scores) == (85.0,)

# plane_angle.py tests
def test_plane_angle_simple():
    a = Point(0, 0, 0)
    b = Point(1, 0, 0)
    c = Point(1, 1, 0)
    d = Point(0, 1, 0)
    assert abs(plane_angle(a, b, c, d) - 0.0) < 0.01 
def test_plane_angle_same_plane():
     a = Point(0, 0, 0)
     b = Point(1, 0, 0)
     c = Point(2, 0, 0)
     d = Point(3, 0, 0)
     assert abs(plane_angle(a, b, c, d) - 0.0) < 0.01 

def test_plane_angle_3d():
    a = Point(1, 0, 0)
    b = Point(0, 1, 0)
    c = Point(0, 0, 1)
    d = Point(1, 1, 1)
    assert abs(plane_angle(a, b, c, d) - 70.52877936550931) < 0.01

# phone_number.py tests
def test_phone_number_sort_simple():
    numbers = ["9195969878", "07895462130", "89875641230"]
    expected = ["+7 (919) 596-98-78", "+7 (789) 546-21-30", "+7 (987) 564-12-30"]
    assert sort_phone(numbers) == expected

def test_phone_number_sort_mix():
    numbers = ["+79195969878", "87895462130", "79875641230"]
    expected = ["+7 (919) 596-98-78", "+7 (789) 546-21-30", "+7 (987) 564-12-30"]
    assert sort_phone(numbers) == expected

# people_sort.py tests
def test_people_sort_simple():
    people = [["Mike", "Thomson", "20", "M"], ["Robert", "Bustle", "32", "M"], ["Andria", "Bustle", "30", "F"]]
    expected = ["Mr. Mike Thomson", "Ms. Andria Bustle", "Mr. Robert Bustle"]
    formatted_names = list(name_format(people))
    assert formatted_names == expected

# complex_numbers.py tests
def test_complex_numbers_add():
    c = Complex(2, 1)
    d = Complex(5, 6)
    assert str(c + d) == "7.00+7.00i"
def test_complex_numbers_subtract():
    c = Complex(2, 1)
    d = Complex(5, 6)
    assert str(c - d) == "-3.00-5.00i"
def test_complex_numbers_multiply():
    c = Complex(2, 1)
    d = Complex(5, 6)
    assert str(c * d) == "4.00+17.00i"
def test_complex_numbers_divide():
    c = Complex(2, 1)
    d = Complex(5, 6)
    assert str(c / d) == "0.26-0.11i"
def test_complex_numbers_mod():
    c = Complex(2, 1)
    assert str(c.mod()) == "2.24+0.00i"
def test_complex_numbers_mod2():
    c = Complex(5, 6)
    assert str(c.mod()) == "7.81+0.00i"

def test_circle_square_mk_r1_n1000():
    r = 1
    n = 1000
    approx_area = circle_square_mk(r, n)
    exact_area = math.pi * r**2
    assert abs(approx_area - exact_area) < 0.5  

def test_circle_square_mk_r2_n10000():
    r = 2
    n = 10000
    approx_area = circle_square_mk(r, n)
    exact_area = math.pi * r**2
    assert abs(approx_area - exact_area) < 0.5 

def test_circle_square_mk_r05_n100000():
    r = 0.5
    n = 100000
    approx_area = circle_square_mk(r, n)
    exact_area = math.pi * r**2
    assert abs(approx_area - exact_area) < 0.1 

# ==================== Тесты для file_sort.py ====================

def test_file_sort_empty_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        result = file_sort(tmpdir)
        assert result == ""

def test_file_sort_mixed_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_a_py = os.path.join(tmpdir, "a.py")
        file_b_py = os.path.join(tmpdir, "b.py")
        file_a_txt = os.path.join(tmpdir, "a.txt")
        file_b_txt = os.path.join(tmpdir, "b.txt")
        
        with open(file_a_py, "w") as f:
             f.write("print('Hello from a.py')")
        with open(file_b_py, "w") as f:
             f.write("print('Hello from b.py')")
        with open(file_a_txt, "w") as f:
             f.write("This is a text file")
        with open(file_b_txt, "w") as f:
             f.write("This is another text file")

        result = file_sort(tmpdir)

        expected_output = 'a.py\nb.py\na.txt\nb.txt'

        assert result == expected_output

def test_file_sort_single_file_type():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.makedirs(os.path.join(tmpdir), exist_ok=True)
        with open(os.path.join(tmpdir, "a.txt"), "w") as f:
            f.write("")
        with open(os.path.join(tmpdir, "b.txt"), "w") as f:
            f.write("")
        result = file_sort(tmpdir)
        expected = "a.txt\nb.txt"
        assert result == expected

def test_file_sort_hidden_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        with open(os.path.join(tmpdir, ".hidden.txt"), "w") as f:
            f.write("")
        result = file_sort(tmpdir)
        assert result == ""

def test_file_sort_with_numbers():
     with tempfile.TemporaryDirectory() as tmpdir:
          os.makedirs(os.path.join(tmpdir), exist_ok=True)
          with open(os.path.join(tmpdir, "1.txt"), "w") as f:
              f.write("")
          with open(os.path.join(tmpdir, "2.txt"), "w") as f:
              f.write("")
          result = file_sort(tmpdir)
          expected = "1.txt\n2.txt"
          assert result == expected

def test_file_sort_different_extensions():
     with tempfile.TemporaryDirectory() as tmpdir:
          os.makedirs(os.path.join(tmpdir), exist_ok=True)
          with open(os.path.join(tmpdir, "file.abc"), "w") as f:
              f.write("")
          with open(os.path.join(tmpdir, "file.xyz"), "w") as f:
              f.write("")
          result = file_sort(tmpdir)
          expected = "file.abc\nfile.xyz"
          assert result == expected

# ==================== Тесты для file_search.py ====================

def test_file_search_found():
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, "testfile.txt")
        with open(test_file, "w") as f:
            f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6")  

        result = file_search(tmpdir, "testfile.txt")

        expected = "Line 1\nLine 2\nLine 3\nLine 4\nLine 5"
        assert result == expected

def test_file_search_not_found():
    with tempfile.TemporaryDirectory() as tmpdir:
        result = file_search(tmpdir, "nonexistent.txt")
        assert result == "Файл nonexistent.txt не найден"

def test_file_search_in_subdirectory():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.makedirs(os.path.join(tmpdir, "subdir"), exist_ok=True)
        test_file = os.path.join(tmpdir, "subdir", "testfile.txt")
        with open(test_file, "w") as f:
            f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6") 

        result = file_search(tmpdir, "testfile.txt")

        expected = "Файл testfile.txt не найден"  
        assert result == expected

def test_file_search_empty_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, "testfile.txt")
        with open(test_file, "w") as f:
            f.write("") 

        result = file_search(tmpdir, "testfile.txt")

        assert result == "" 

def test_file_search_with_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, "testfile.txt")
        with open(test_file, "w") as f:
            f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6")

        result = file_search(tmpdir, os.path.basename(tmpdir)) 
        assert result == "Файл " + os.path.basename(tmpdir) + " не найден"