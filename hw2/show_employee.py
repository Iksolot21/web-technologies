def show_employee(name, salary=100000):
    return f"{name}: {salary} $"

if __name__ == '__main__':
    print(show_employee("Alice"))
    print(show_employee("Bob", 50000))