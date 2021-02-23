import sys

def draw_star(i, j):
    while i != 0:
        # 몫이 1이라면
        if i % 3 == 1 and j % 3 == 1:
            sys.stdout.write(' ')
            return None
        # 3으로 나누어서 위 if문에 걸리면 그 부분도 빈칸 처리
        i //= 3
        j //= 3
    sys.stdout.write('*')

n = int(input())
for i in range(n):
    for j in range(n):
        draw_star(i, j)
    sys.stdout.write('\n')
