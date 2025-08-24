ls = []
while True:
    a, b = map(int, input().split())

    if a ==0 and b==0:
        break

    ls.append(a+b)
    

for i in ls:
    print(i)