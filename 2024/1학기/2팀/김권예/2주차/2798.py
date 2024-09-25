# 2798. 블랙잭
# N개의 카드 수에서 3장을 뽑은 후,
# 3장의 합이 M을 넘지 않고 가장 가까운 수로 만들기

N, M = map(int,input().split())
card = list(map(int,input().split()))
best = 0

# 3중 for문으로 모든 경우의 수를 확인
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            # 3개의 카드의 합이 M 보다 크다면 넘김
            if card[i]+card[j]+card[k] > M : 
                continue
            
            # 새로운 조합과 저장된 이전의 값과 비교하여 더 큰 값으로 갱신
            else : 
                best = max(best, card[i]+card[j]+card[k]) 

print(best)