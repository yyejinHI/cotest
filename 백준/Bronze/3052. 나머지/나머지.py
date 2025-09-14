import sys

num_list = []
result = []

for i in range(0,10):
    a = int(sys.stdin.readline())
    num_list.append(a)


for k in num_list:
    result.append(k % 42)

print(len(set(result))) 