import sys
put = sys.stdin.readline
n = int(put().rstrip())
for _ in range(n):
    a, b = list(map(int, put().rstrip().split()))
    print(a+b)







