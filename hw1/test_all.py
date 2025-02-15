import subprocess
import pytest
import os  

INTERPRETER = 'python'  

def run_script(filename, input_data=None):
    """Запускает скрипт и возвращает вывод."""
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'python_if_else': [
        ('1', 'Weird'),
        ('2', 'Not Weird'),
        ('3', 'Weird'),
        ('4', 'Not Weird'),
        ('5', 'Weird'),
        ('6', 'Weird'),
        ('20', 'Weird'),
        ('22', 'Not Weird'),
        ('100', 'Not Weird')  
    ],
    'arithmetic_operators': [
        (['5', '3'], ['8', '2', '15']),
        (['-5', '3'], ['-2', '-8', '-15']),
        (['0', '0'], ['0', '0', '0']),
        (['10', '5'], ['15', '5', '50']),  
        (['1000', '1'], ['1001', '999', '1000'])  
    ],
    'division': [
        (['10', '2'], ['5', '5.0']),
        (['0', '5'], ['0', '0.0']),
        (['5', '0'], ['0', 'inf']), 
        (['7', '3'], ['2', '2.3333333333333335'])
    ],
    'loops': [
        (['4'], ['0', '1', '4', '9']),
        (['1'], ['0']),
        (['0'], []),  
        (['2'], ['0', '1']),
        (['5'], ['0', '1', '4', '9', '16'])
    ],
    'print_function': [
        (['5'], '12345'),
        (['1'], '1'),
        (['2'], '12'),
        (['10'], '12345678910')
    ],
    'second_score': [
    (['5', '2 3 6 6 5'], ['5']),
    (['5', '2 2 2 3 3'], ['2']), 
    (['5', '-5 -3 -2 -2 -1'], ['-2']),
    (['3', '5 5 5'], ['5']),
    (['4', '1 2 2 3'], ['2'])  
],
    'nested_list': [
        (['5', 'Гарри', '37.21', 'Берри', '37.21', 'Тина', '37.2', 'Акрити', '41', 'Харш', '39'], ['Берри', 'Гарри']),
        (['3', 'Алиса', '50.0', 'Боб', '50.0', 'Чарли', '40.0'], ['Алиса', 'Боб']),
        (['2', 'Алиса', '50.0', 'Боб', '50.0'], ['Алиса', 'Боб'])
    ],
    'lists': [
        (['12', 'insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print'], ['[6, 5, 10]', '[1, 5, 9, 10]', '[9, 5, 1]']),
        (['0'], []),
        (['5', 'insert 0 5', 'insert 1 5', 'print', 'remove 5', 'print'], ['[5, 5]', '[5]']),
        (['4', 'append 1', 'append 2', 'insert 1 3', 'print'],['[1, 3, 2]'])
    ],
    'swap_case': [
        (['HackerRank.com presents Pythonist 2'], ['hACKERrANK.COM PRESENTS pYTHONIST 2']),
        ([''], ['']),
        (['123abcABC'], ['123ABCabc']),
        (['Www.MosPolytech.ru'], ['wWW.mOSpOLYTECH.RU'])
    ],
    'split_and_join': [
        (['this is a string'], ['this-is-a-string']),
        ([''], ['']),
        (['this   is   a   string'], ['this-is-a-string']),
        (['one two three'], ['one-two-three'])
    ],
    'anagram': [
        (['listen', 'silent'], ['YES']),
        (['hello', 'world'], ['NO']),
        (['Listen', 'silent'], ['NO']),
        (['a', 'b'], ['NO'])  
    ],
    'metro': [
        (['2', '0 10', '5 15', '7'], ['2']),
        (['2', '0 5', '6 10', '12'], ['0']),
        (['2', '0 5', '5 10', '5'], ['2']),
        (['1', '0 10', '5'], ['1'])
    ],
    'minion_game': [
        (['BANANA'], ['Stuart 12']), 
        (['AEIOU'], ['Kevin 15']),   
        (['BAA'], ['Tie']),       
        ([''], ['Tie'])           
    ],
    'is_leap': [
        (['2024'], ['True']),
        (['2021'], ['False']),
        (['2100'], ['False']),
        (['2000'], ['True']),
        (['1900'], ['False'])
    ],
    'happiness': [
    (['3 2', '1 5 3', '3 1', '5 7'], ['1']),
    (['3 2', '1 5 3', '3 1', '5 7'], ['1']),
    (['3 2', '1 5 3', '2 4', '6 7'], ['0']),
],
     'pirate_ship': [
    (['10 2', 'item1 5 10', 'item2 5 12'], ['item2 5.0 12.00', 'item1 5.0 10.00']),
    (['5 1', 'item1 6 10'], ['']),
    (['10 1', 'item1 5 25'], ['item1 5.0 25.00'])
    ],
    'matrix_mult': [
        (['2', '1 2', '3 4', '5 6', '7 8'], ['19 22', '43 50']),
        (['3', '1 2 3', '4 5 6', '7 8 9', '9 8 7', '6 5 4', '3 2 1'], ['30 24 18', '84 69 54', '138 114 90']),
        (['1', '5', '3'], ['15'])
    ]
}

def test_hello_world():
    assert run_script('hello.py') == 'Hello, World!'

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    output = run_script('loops.py', input_data)
    expected_lines = expected if expected else []
    output_lines = output.split('\n') if output else []
    assert output_lines == expected_lines

@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', [input_data[0], input_data[1]]).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    if expected:
        output = run_script("nested_list.py", input_data).split('\n')
        assert sorted(output) == sorted(expected)
    else:
        assert run_script("nested_list.py", input_data) == ""


@pytest.mark.parametrize("input_data, expected", test_data['lists'])
def test_lists(input_data, expected):
    output = run_script("lists.py", input_data)
    expected_lines = expected if expected else []
    output_lines = output.split('\n') if output else []
    assert output_lines == expected_lines

@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data) == expected[0]

@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data) == expected[0]

@pytest.mark.parametrize("input_data, expected", test_data['anagram'])
def test_anagram(input_data, expected):
    output = run_script('anagram.py', input_data).strip()
    assert output == expected[0]


@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    output = run_script('happiness.py', input_data)
    if input_data[2] == '' and input_data[3] == '':
        assert output.strip() == expected[0]
    else:
        assert output.strip() == expected[0]

@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    result = run_script("minion_game.py", input_data)
    if input_data[0] == "":
        assert result == ""
    else:
        result = result.replace("Стюарт", "Stuart").replace("Кевин", "Kevin").replace("Ничья","Tie")
        assert result == expected[0]

@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    output = run_script('pirate_ship.py', input_data).split('\n')
    if not expected:
        assert output == ['']
    else:
        assert sorted(output) == sorted(expected)



@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data).split('\n') == expected


def test_max_word():
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("This is a test file.  It contains some long words like supercalifragilisticexpialidocious and antidisestablishmentarianism.")
    expected_output = "supercalifragilisticexpialidocious"
    assert "\n".join(sorted(run_script("max_word.py").splitlines())) ==  expected_output


def test_price_sum():
    with open("products.csv", "w", newline="") as f:
        f.write("category,expense\nвзрослый,10.50\nпенсионер,5.25\nребёнок,2.75\nвзрослый,5.00")
    assert run_script("price_sum.py") == "15.5 5.25 2.75"
    os.remove("products.csv")