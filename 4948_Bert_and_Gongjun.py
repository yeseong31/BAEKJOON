# 베르트랑 공준
# 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재

x = 123456 * 2 + 1
prime = [True] * x

for i in range(2, int(x * 0.5) + 1):
    if prime[i]:
        for j in range(2 * i, x, i):
            prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if prime[i]:
            count += 1
    print(count)


