import sys

n = int(sys.stdin.readline()) #충격...
#sys.stdin.readline()은 우리가 입력한 글자뿐만 아니라, 
#글자를 입력하고 마지막에 누르는 엔터(Enter) 키까지 함께 읽어 들임
li = []

for i in range(0,n):
    s = sys.stdin.readline().strip()
    li.append(s)

for k in range(0, len(li)):
    print(li[k][0] + li[k][-1]) # [-1]이 안 먹히는게 아니라 개행 문자를 읽어오고 있었다...