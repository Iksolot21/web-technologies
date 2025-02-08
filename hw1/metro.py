n = int(input())
entries = []
exits = []
for _ in range(n):
    a, b = map(int, input().split())
    entries.append(a)
    exits.append(b)

t = int(input())
count = 0
for i in range(n):
    if entries[i] <= t <= exits[i]:
        count += 1

print(count)