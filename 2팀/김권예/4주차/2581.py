# 2581. 소수
# N 이상 M 이하의 자연수 중 소수를 찾아,
# 소수의 합과 최소값을 찾아내기

n = int(input())
m = int(input())
cnt = []

for i in range(n, m+1):
    if i > 1 : # 중요! 2 이상의 수들 중에서 소수를 찾음
        prime = True
        for j in range(2, i):
            if i % j == 0 : # 나머지가 0이라면 -> 소수가 아니라면
                prime = False
                break
        if prime : # prime이 True 라면
            cnt.append(i) # 소수 배열에 추가
        
if cnt : # cnt가 비어있지 않다면
    print(sum(cnt), cnt[0], sep='\n')
else : # cnt가 비어있다면 -> 소수가 없다는 말도 되지만, n,m이 1이라는 조건에도 작동함
    print(-1)
