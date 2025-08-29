a = input()
a_new = []
# 문자열 자체가 list 일텐데
for i in a:
    if i.isupper() == True:
        a_new.append(i.lower())
    elif i.islower() == True:
        a_new.append(i.upper())

print(''.join(a_new)) #list를 문자열로 변환 
# "합치면서 중간에 넣고 싶은 거".join( list )