def matrix_multiply(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == "__main__":
    n = int(input())
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))
    B = []
    for _ in range(n):
        B.append(list(map(int, input().split())))

    C = matrix_multiply(A, B)

    for row in C:
        print(*row)