import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num_s = set(num) #set[0]은 이렇게 출력 불가능
num_l = list(num_s)
num_l.sort() 
# list.sort()는 원본을 변경
# (얘 자체는 아무것도 return하지 않음, 그냥 원본만 바꾸는 효과)
# sorted(list)는 원본 그대로, 정렬된 list를 리턴함

print(num_l[0], num_l[-1])