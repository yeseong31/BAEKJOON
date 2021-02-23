# 팩토리얼

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input())
print(factorial(n))

# 재귀를 활용한 팩토리얼 알고리즘 구현은 시간 복잡도 측면에서 굉장히 비효율적이다.
# '다이나믹 프로그래밍' 방법을 활용하면 효율성을 개선할 수 있다.

n = int(input())
d = [0] * (n + 1)
d[1] = 1
for i in range(2, n + 1):
    d[i] = i * d[i - 1]
print(d[n])
