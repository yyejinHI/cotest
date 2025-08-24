n = int(input())
n_list = []

for i in range(0, n):
    a, b = map(int, input().split())
    n_list.append(a+b)

# for j in range(0,n):
#     print(n_list[j])

for j in n_list:
    print(j)