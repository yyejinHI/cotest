import sys
import math

a, b, v = map(int, sys.stdin.readline().split())

days = math.ceil((v - a) / (a - b)) + 1

print(days)