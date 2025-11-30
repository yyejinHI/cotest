import sys

n,m = map(int, sys.stdin.readline().split())

A, B = [], []


for row in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    A.append(row)

for row in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    B.append(row)


for i in range(n):
    for j in range(m):
        result = A[i][j] + B[i][j]
        print(result, end = ' ')
    print()