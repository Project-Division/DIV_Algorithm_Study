# 11659 구간 합 구하기 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num_list = list(map(int, input().split()))

sum = 0
sum_list = [0]
for num in num_list:
    sum += num
    sum_list.append(sum)

for _ in range(m):
    x, y = map(int, input().split())
    print(sum_list[y] - sum_list[x-1])