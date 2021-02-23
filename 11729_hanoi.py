# 하노이

def hanoi(n, start, mid, end):
    if n < 1:
        return
    global count, arr
    # n - 1번까지의 원반을 2번으로 옮김
    hanoi(n - 1, start, end, mid)
    # n번 원반을 3번으로 옮김
    arr.append((start, end))
    count += 1
    # n - 1번까지의 원반을 3번으로 옮김
    hanoi(n - 1, mid, start, end)

n = int(input())
count = 0
arr = []

hanoi(n, 1, 2, 3)
print(count)
for a, b in arr:
    print(a, b)
