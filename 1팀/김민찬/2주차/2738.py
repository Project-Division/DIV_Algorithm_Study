#https://www.acmicpc.net/problem/2738

# 입력 받기
N, M = map(int, input().split())

# 행렬 A 입력 받기
matrix_A = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix_A.append(row)

# 행렬 B 입력 받기
matrix_B = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix_B.append(row)

# 행렬 덧셈
result_matrix = []
for i in range(N):
    result_row = []
    for j in range(M):
        result_row.append(matrix_A[i][j] + matrix_B[i][j])
    result_matrix.append(result_row)

# 결과 출력
for row in result_matrix:
    print(*row)
