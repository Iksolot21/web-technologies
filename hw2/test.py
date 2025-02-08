import subprocess
import pytest
import math
import os
import re

INTERPRETER = 'python3'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

# Импортируйте ваши функции
from fact import fact_rec, fact_it
from show_employee import show_employee
from sum_and_sub import sum_and_sub
from process_list import process_list, process_list_comprehension, process_list_gen
from my_sum import my_sum
from email_validation import fun, filter_mail
from fibonacci import fibonacci, cube
from average_scores import compute_average_scores
from plane_angle import Point, plane_angle
from phone_number import sort_phone, wrapper
from people_sort import person_lister, name_format
from complex_numbers import Complex
from circle_square_mk import circle_square_mk
from log_decorator import function_logger #Тесты опциональны

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
    assert abs(plane_angle(a, b, c, d) - 90.0) < 0.01 # Allow small floating-point error

def test_plane_angle_same_plane():
     a = Point(0, 0, 0)
     b = Point(1, 0, 0)
     c = Point(2, 0, 0)
     d = Point(3, 0, 0)
     assert abs(plane_angle(a, b, c, d) - 180.0) < 0.01 # Allow small floating-point error

def test_plane_angle_3d():
    a = Point(1, 0, 0)
    b = Point(0, 1, 0)
    c = Point(0, 0, 1)
    d = Point(1, 1, 1)
    assert abs(plane_angle(a, b, c, d) - 61.87) < 0.01

# phone_number.py tests
def test_phone_number_sort_simple():
    numbers = ["9195969878", "07895462130", "89875641230"]
    expected = ["+7 (789) 546-21-30", "+7 (919) 596-98-78", "+7 (987) 564-12-30"]
    assert sort_phone(numbers) == expected
def test_phone_number_sort_mix():
    numbers = ["+79195969878", "87895462130", "79875641230"]
    expected = ["+7 (789) 546-21-30", "+7 (919) 596-98-78", "+7 (987) 564-12-30"]
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
    assert abs(approx_area - exact_area) < 0.5  # adjust tolerance as needed

def test_circle_square_mk_r2_n10000():
    r = 2
    n = 10000
    approx_area = circle_square_mk(r, n)
    exact_area = math.pi * r**2
    assert abs(approx_area - exact_area) < 0.5 # adjust tolerance as needed

def test_circle_square_mk_r05_n100000():
    r = 0.5
    n = 100000
    approx_area = circle_square_mk(r, n)
    exact_area = math.pi * r**2
    assert abs(approx_area - exact_area) < 0.1 # adjust tolerance as needed
import tempfile
import os
import pytest

def test_files_sort_empty_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        result = run_script('files_sort.py', input_data=[tmpdir])
        assert result == ""

def test_files_sort_mixed_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Создаем тестовые файлы
        os.makedirs(os.path.join(tmpdir), exist_ok=True) # Create the directory
        with open(os.path.join(tmpdir, "a.py"), "w") as f:
            f.write("")
        with open(os.path.join(tmpdir, "a.txt"), "w") as f:
            f.write("")
        with open(os.path.join(tmpdir, "b.py"), "w") as f:
            f.write("")
        with open(os.path.join(tmpdir, "b.txt"), "w") as f:
            f.write("")
        
        # Запускаем скрипт и проверяем результат
        result = run_script('files_sort.py', input_data=[tmpdir]).split('\n') # Pass tmpdir as input data
        expected = ["a.py", "b.py", "a.txt", "b.txt"] # The exact sorted order
        assert result == expected

def test_files_sort_single_file_type():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Создаем тестовые файлы
        os.makedirs(os.path.join(tmpdir), exist_ok=True) # Create the directory
        with open(os.path.join(tmpdir, "a.txt"), "w") as f:
            f.write("")
        with open(os.path.join(tmpdir, "b.txt"), "w") as f:
            f.write("")
        result = run_script('files_sort.py', input_data=[tmpdir]).split('\n') # Pass tmpdir as input data
        expected = ["a.txt", "b.txt"]
        assert result == expected

def test_files_sort_hidden_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a hidden file
        with open(os.path.join(tmpdir, ".hidden.txt"), "w") as f:
            f.write("")
        # Execute script and verify the hidden file is not listed
        result = run_script('files_sort.py', input_data=[tmpdir]).split('\n') # Pass tmpdir as input data
        assert result == []

def test_files_sort_with_numbers():
     with tempfile.TemporaryDirectory() as tmpdir:
          os.makedirs(os.path.join(tmpdir), exist_ok=True)
          with open(os.path.join(tmpdir, "1.txt"), "w") as f:
              f.write("")
          with open(os.path.join(tmpdir, "2.txt"), "w") as f:
              f.write("")
          result = run_script('files_sort.py', input_data=[tmpdir]).split('\n')
          expected = ["1.txt", "2.txt"]
          assert result == expected

def test_files_sort_different_extensions():
     with tempfile.TemporaryDirectory() as tmpdir:
          os.makedirs(os.path.join(tmpdir), exist_ok=True)
          with open(os.path.join(tmpdir, "file.abc"), "w") as f:
              f.write("")
          with open(os.path.join(tmpdir, "file.xyz"), "w") as f:
              f.write("")
          result = run_script('files_sort.py', input_data=[tmpdir]).split('\n')
          expected = ["file.abc", "file.xyz"]
          assert result == expected

def test_file_search_found():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create the test file
        test_file = os.path.join(tmpdir, "testfile.txt")
        with open(test_file, "w") as f:
            f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6")  # Add more lines than will be output

        # Run the script
        result = run_script('file_search.py', input_data=["testfile.txt"]).split('\n') # Search for file relative to script's dir

        # Verify the output
        expected = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5"] # Check the first 5 lines of the file
        assert result == expected

def test_file_search_not_found():
    result = run_script('file_search.py', input_data=["nonexistent.txt"])
    assert result == "Файл nonexistent.txt не найден"

def test_file_search_in_subdirectory():
     with tempfile.TemporaryDirectory() as tmpdir:
        # Create the test file
        os.makedirs(os.path.join(tmpdir, "subdir"), exist_ok=True) # Create subdirectory
        test_file = os.path.join(tmpdir, "subdir", "testfile.txt")
        with open(test_file, "w") as f:
             f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6") # Create a sample file

        # Run the script
        result = run_script('file_search.py', input_data=["testfile.txt"])

        # Verify the output
        expected = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5"]
        assert result == expected

def test_file_search_empty_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create the test file
        test_file = os.path.join(tmpdir, "testfile.txt")
        with open(test_file, "w") as f:
            f.write("") # Create an empty file
        
        # Run the script
        result = run_script('file_search.py', input_data=["testfile.txt"]).split('\n') # Search for file

        # Verify the output
        assert result == [''] # Verify output

def test_file_search_with_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test file
        test_file = os.path.join(tmpdir, "testfile.txt")
        with open(test_file, "w") as f:
            f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6")

        # Try searching for directory instead of file
        result = run_script('file_search.py', input_data=[tmpdir])
        assert result == "Файл " + tmpdir + " не найден"
def test_my_sum_argv_no_args():
    result = run_script('my_sum_argv.py')
    assert result == "" #  Ожидаемый вывод, если аргументы не переданы.

def test_my_sum_argv_positive():
    result = run_script('my_sum_argv.py', input_data=['1', '2', '3']) # Передаем ввод как список строк
    assert result == "6.0"

def test_my_sum_argv_negative():
    result = run_script('my_sum_argv.py', input_data=['-1', '-2', '-3']) # Передаем ввод как список строк
    assert result == "-6.0"

def test_my_sum_argv_mixed():
    result = run_script('my_sum_argv.py', input_data=['1', '-2', '3', '-4']) # Передаем ввод как список строк
    assert result == "-2.0"

def test_my_sum_argv_float():
    result = run_script('my_sum_argv.py', input_data=['1.5', '2.5', '3.5']) # Передаем ввод как список строк
    assert result == "7.5"

def test_my_sum_argv_single_arg():
    result = run_script('my_sum_argv.py', input_data=['5'])
    assert result == "5.0"