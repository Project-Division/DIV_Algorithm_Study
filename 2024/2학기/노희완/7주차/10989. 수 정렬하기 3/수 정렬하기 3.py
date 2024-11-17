# 10989 수 정렬하기 3

import sys

n = int(sys.stdin.readline().rstrip())

count = [0] * 10001
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    count[num] += 1

for j in range(len(count)):
    if (count[j] > 0):
        for k in range(count[j]):
            print(j)