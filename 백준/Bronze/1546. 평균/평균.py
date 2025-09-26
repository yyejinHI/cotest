import sys

n = int(sys.stdin.readline())

real = []
notreal = []
sum = 0

real = list(map(int, sys.stdin.readline().split()))
real.sort()

for r in range(len(real)):
    b = real[r]/real[-1]*100
    notreal.append(b)

for m in notreal:
    sum += m 

print(sum/len(notreal))