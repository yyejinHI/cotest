import sys

m, n = map(int, sys.stdin.readline().split())

# 1. n+1 크기의 체(목록)를 만들고, 모두 소수(True)라고 가정한다.
# 0번, 1번 인덱스는 사용 편의를 위해 그대로 둔다.
is_prime = [True] * (n + 1)

# 2. 0과 1은 소수가 아니므로 False로 표시한다.
if n >= 1:
    is_prime[0] = is_prime[1] = False

# 3. 2부터 n의 제곱근까지만 반복한다.
# i*i > n 이면 더 이상 확인할 필요가 없다.
for i in range(2, int(n**0.5) + 1):
    # 만약 i가 소수라면,
    if is_prime[i]:
        # i의 배수들을 모두 소수가 아니라고 표시한다.
        # i*i 이전의 배수들은 이미 다른 소수의 배수로서 지워졌다.
        for j in range(i*i, n + 1, i):
            is_prime[j] = False

# 4. m부터 n까지의 숫자 중에서, 체에 소수(True)라고 표시된 숫자만 출력한다.
for i in range(m, n + 1):
    if is_prime[i]:
        print(i)