import sys

n = int(sys.stdin.readline())
# li = [] ## 이렇게 하면 메모리 초과 발생

# for i in range(n):
#     a = int(sys.stdin.readline().strip()) # 뒤에 개행문자 빼고 입력받으려면 .strip()
#     li.append(a)

# li.sort() #그냥 바로 원본에 정렬은 .sort()

# for k in li:
#     print(k)

count_box = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    count_box[num] += 1

for i in range(1, 10001):
    if count_box[i] != 0:
        for _ in range(count_box[i]):
            print(i)