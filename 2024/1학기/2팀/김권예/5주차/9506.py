# 9506. 약수들의 합
# 자신을 제외한 약수들의 합과 자신이 같으면 완전수라고 함
# 완전수 판별 코드

while True:
    n = int(input())
    f = []
    if n == -1 : # 입력의 마지막엔 -1
        break
    
    for i in range(1, n): 
        if n % i == 0 : # 약수를 찾으면 리스트에 저장
            f.append(i)
            
    if sum(f) == n : # 리스트(약수)의 합이 n과 같다면 -> 완전수라면
        # '사이에 추가할 문자'.join(리스트)
        print(n,"=", ' + '.join(map(str, f)))
    else :
        print("%d is NOT perfect."%n)