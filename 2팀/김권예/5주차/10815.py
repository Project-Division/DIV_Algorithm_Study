# 10815. 숫자 배열
# 집합과 맵

N = int(input())
NN = set(map(int, input().split()))

M = int(input())
MM = list(map(int, input().split()))

for i in MM: 
    r = 0 # 초기 결과값 r을 0으로 설정
    if i in NN: # 만약 현재 원소 i가 집합 NN에 있으면
        r = 1 # 결과값 r을 1로 변경
    print(r, end=" ")
 