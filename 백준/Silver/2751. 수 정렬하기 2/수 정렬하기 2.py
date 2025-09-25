import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
    j = int(sys.stdin.readline())
    li.append(j)

li.sort()

for i in li:
    print(i)