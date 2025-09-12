import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

result = str(A*B*C)
result_list = [0,0,0,0,0,0,0,0,0,0]

for i in result :
    for k in range(0,10):
        i_int = int(i)
        if i_int == k:
            result_list[k] += 1


for a in result_list:
    print(a)