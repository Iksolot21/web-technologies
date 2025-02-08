import csv

def calculate_expenses(filename="products.csv"):
    adult = 0
    pensioner = 0
    child = 0

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) 

        for row in reader:
            category, expense = row
            expense = float(expense)

            if category == "взрослый":
                adult += expense
            elif category == "пенсионер":
                pensioner += expense
            elif category == "ребёнок":
                child += expense

    return round(adult, 2), round(pensioner, 2), round(child, 2)


if __name__ == "__main__":
    adult_expenses, pensioner_expenses, child_expenses = calculate_expenses()
    print(adult_expenses, pensioner_expenses, child_expenses)