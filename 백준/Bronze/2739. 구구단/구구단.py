n = int(input())

# for i in range(1, 10):
#     print(str(n) + " * " + str(i) + " = " + str(n*i) )

# for i in range(1, 10):
#     print(f"{n} * {i} = {n*i}") # 훨씬 깔끔하다


for i in range(1, 10):
    print("{} * {} = {}".format(n, i, n*i))