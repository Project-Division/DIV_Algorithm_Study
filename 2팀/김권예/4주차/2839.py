# 2839. 설탕 배달 (브루트 포스)

n = int(input())
cnt = 0 # 운반 개수

# 최소 경우
if n % 5 == 0 : # 5kg로 전부 가능할 때
    print(n // 5)
else : # 3kg, 5kg 로 나눠서 운반해야할 때
    while True:
        if n % 5 != 0: # 5로 나눠지지 않을 때
            n = n - 3 # + 3kg
            cnt += 1
        elif n % 5 == 0:
            cnt += n // 5
            print(cnt)
            break
        if n < 0:
            print(-1)
            break