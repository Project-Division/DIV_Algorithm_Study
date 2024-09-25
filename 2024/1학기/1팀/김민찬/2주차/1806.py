#https://www.acmicpc.net/problem/1806

import sys

def min_subarray_length(N, S, sequence):
    left = right = total = 0
    min_length = float('inf')

    while right < N:
        total += sequence[right]
        while total >= S:
            min_length = min(min_length, right - left + 1)
            total -= sequence[left]
            left += 1
        right += 1

    return min_length if min_length != float('inf') else 0

# 입력 받기
N, S = map(int, input().split())
sequence = list(map(int, input().split()))

# 결과 출력
result = min_subarray_length(N, S, sequence)
print(result)
