## 이 문제는 문자열 활용하는 문제
# S = "baekjoon"

# print(S.find('b'))  # 결과: 0 ('b'는 0번째 위치에 처음 나옴)
# print(S.find('a'))  # 결과: 1 ('a'는 1번째 위치에 처음 나옴)
# print(S.find('k'))  # 결과: 4 ('k'는 4번째 위치에 처음 나옴)
# print(S.find('z'))  # 결과: -1 ('z'는 단어에 없으므로 -1)


import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"

result =[]

S = sys.stdin.readline()

for char in alphabet:
    result.append(S.find(char))

print(" ".join(map(str, result)))