# 골드바흐

# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다.
# 또한, 짝수를 두 소수의 합으로 나타내는 표현을 '골드바흐 파티션'이라 한다.
# n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오.
# 골드바흐 파티션이 여러 개인 경우에는 두 소수의 차이가 가장 작은 것을 출력.

# 에라토스테네스의 체
def prime_lst(n):
    d = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if d[i]:
            for j in range(i * 2, n, i):
                d[j] = False
    return [i for i in range(2, n) if d[i]]

def goldbach(n):
    lst = prime_lst(n)
    index = max([i for i in range(len(lst)) if lst[i] <= n // 2])
    for i in range(index, -1, -1):
        for j in range(i, len(lst)):
            if lst[i] + lst[j] == n:
                return [lst[i], lst[j]]

for _ in range(int(input())):
    g = goldbach(int(input()))
    print(g[0], g[1])
        

    
