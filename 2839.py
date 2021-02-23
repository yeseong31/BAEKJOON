# 설탕 배달
# 3kg, 5kg 설탕 봉지 조합으로
# 만들 수 있는 최소 설탕 봉지 수

n = int(input())
d = [5001] * (n + 1)

d[0] = 0
for i in [3, 5]:
    for j in range(i, n + 1):
        d[j] = min(d[j], d[j - i] + 1)
print(-1 if d[n] == 5001 else d[n])
