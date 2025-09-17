import sys

S = sys.stdin.readline()

print(len(list(S.split()))) 
# split()은 모든 공백 지워줌 
# split(" ")은 중간에 있는 공백만을 기준으로 분리