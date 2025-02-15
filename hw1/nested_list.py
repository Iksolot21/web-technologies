students = []
n = int(input())  
for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(list(set([score for name, score in students])))

if len(scores) > 1:  
    second_lowest = scores[1]
    second_lowest_students = [name for name, score in students if score == second_lowest]
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)
elif len(scores) == 1 and n > 1:
    second_lowest = scores[0]
    second_lowest_students = [name for name, score in students if score == second_lowest]
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)
else:
    pass