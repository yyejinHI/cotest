import sys

l = {int(input()) for _ in range(28)}
st_l = {i for i in range(1,31)}

st = list(st_l - l) #st = list(st_l - l).sort() --> 여기서 바로 정렬은 안 됨 
st.sort()

# for i in st: 
#     print(i)

# print("\n".join(st))

print("\n".join(map(str, st))) #map(int, input().split())
#join: list -> 문자열
#map(str, st) 2, 8 각각의 숫자를 str으로 변경 