import sys 

li = list(map(int, sys.stdin.readline().split()))

asc_li = [1,2,3,4,5,6,7,8]
desc_li = [8,7,6,5,4,3,2,1]

if li == asc_li:
    print("ascending")
elif li == desc_li:
    print("descending")
else:
    print("mixed")