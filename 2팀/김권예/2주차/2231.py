# 분해합
# ex. 245의 분해합 245+2+4+5 = 256
# 245는 256의 생성자
# 가장 작은 생성자 구하기

n = int(input())
result = 0

for i in range(1,n+1):
    # str로 바꾸고 각 자리를 더하여 m에 저장
    m = sum(map(int, str(i)))
    if i + m == n:
        # 생성자를 발견한다면 i 값에 저장하고 break
        result = i
        break
    
print(result)