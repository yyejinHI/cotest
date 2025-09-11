import sys

n = int(sys.stdin.readline())

li = input()
total = 0

for a in li:
    a_int = int(a)
    total += a_int

print(total)