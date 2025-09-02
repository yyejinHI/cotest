y = int(input())

# if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
#     print(1)
# else:
#     print(0)

#한 줄로 쓰기 
# print(1 if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 0 )

#불리언 이용하기 
print(int((y % 4 == 0 and y % 100 != 0) or y % 400 == 0))