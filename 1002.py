# 터렛

# 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    r = sorted([d, r1, r2])
    res = -1 if (d == 0 and r1 == r2)else 1 if (r1 + r2 == d or abs(r1 - r2) == d) else 0 if (r[2] > r[0] + r[1]) else 2
    print(res)
