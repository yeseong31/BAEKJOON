# 피보나치 수 5

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

print(fibo(int(input())))

# 재귀함수를 이용한 피보나치 수열 알고리즘은 굉장히 비효율적이라는 것을 알아둘 것.
# '메모이제이션' 방법을 이용하면 더 효율적으로 알고리즘을 구현할 수 있다.
# 다만, 메모리 측면에서는 비효율적일 수도 있다.

n = int(input())
d = [0] * (n + 1)
d[1] = d[2] = 1
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
print(d[n])
