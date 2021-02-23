
def star(n):
    global arr
    # 가장 작은 별 모양 단위(재귀 탈출 조건)
    if n == 3:
        arr[0][:3] = arr[2][:3] = ['*'] * 3
        arr[1][:3] = ['*', ' ', '*']
        return
    m = n // 3
    star(m)
    
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(m):
                arr[m*i+k][m*j:m*(j+1)] = arr[k][:m]    # 핵심

n = int(input())
arr = [[' '] * n for _ in range(n)]
star(n)
print('\n'.join([''.join([i for i in row]) for row in arr]))

