n = int(input())
arr = list(map(int, input().split()))
arr = sorted(list(set(arr)))
if len(arr) >= 2:
    print(arr[-2])
else:
    print(arr[0])