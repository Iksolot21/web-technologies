def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = input().strip()  # Убираем лишние пробелы и переводы строк
s2 = input().strip()

if are_anagrams(s1, s2):
    print("YES")
else:
    print("NO")
