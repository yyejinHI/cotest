import sys


while True:
    a = list(map(int, sys.stdin.readline().split()))
    
    if a[0] ==0 or a[1]==0 or a[2]==0:
        break

    a.sort()

    if a[0]**2 + a[1]**2 == a[2]**2:
        print("right")
    else:
        print("wrong")