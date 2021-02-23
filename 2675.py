import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    repeat, s = input().split()
    for i in s:
        print(i * int(repeat), end='')
    print()
