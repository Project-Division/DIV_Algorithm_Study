# 입력 받기
N, M = map(int, input().split())

# N과 M 중 작은 값을 선택하여 해당 값에서 1을 뺀 횟수만큼 쪼개면 최소 쪼개기 횟수
min_splits = min(N, M) - 1

print(min_splits)
