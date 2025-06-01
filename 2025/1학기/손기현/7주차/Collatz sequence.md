# 문제  
## 현재값이 x이면 짝수일 때 나누기 2, 홀수 3*x + 1 반복해 x = 1이 될 때의 과정을 리턴하여라라
## [링크](https://school.programmers.co.kr/learn/courses/30/lessons/181919)
## 코드
    """ python3
    def solution(n):
    answer = []
    while True:
        if n == 1:
            answer.append(n)
            break
        if n % 2 == 0:
            answer.append(n)
            n = n//2
        else:
            answer.append(n)
            n = 3 * n + 1
        
    return answer


    """
## 요점
콜라츠 수열은 짝수 일 때, 2로 나누고 홀 수 라면 3을 곱하고 1을 더하길 반복하면 1이 되는냐 묻는 문제로
1000 이하에서는 1이 된다는 검증에 1000 이하의 수를 다루기 때문에 예외처리를 따로 하지않고고
무한 반복을 돌려서 1이면 1을 answer에 더하여 반복문을 끝내는데, 짝수일 때 2로 나누고, 홀 수 라면 3을 곱하고 1을 더하기를 반복하게하는 코드를 완성했습니다.