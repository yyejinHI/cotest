import sys

ab = []
while True:
    try:
        a, b = map(int, input().split())
        ab.append(a+b)
    except EOFError:
        break

for i in ab:
    print(i)