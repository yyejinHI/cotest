import sys

n = int(sys.stdin.readline())

n_li = []
S_li = []

for i in range(0,n):
    k, s = map(str, sys.stdin.readline().split())
    n_li.append(k)
    S_li.append(s)

n_li = list(map(int, n_li))

for i in range(0, len(n_li)):
    result = "".join([char*n_li[i] for char in S_li[i]])
    print(result)
