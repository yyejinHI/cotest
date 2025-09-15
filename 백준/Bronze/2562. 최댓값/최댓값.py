import sys

n = []

for i in range(0,9):
    a = int(sys.stdin.readline())
    n.append(a)

n_sort = sorted(n)

max_index = n.index(n_sort[8])


print(n_sort[8])
print(max_index+1)