# 문제 
## 주사위를 3번 굴려 값이 모두 같으면 (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3) 모두 다르면 a + b + c 두가지만 같으면 (a + b + c) * (a**2 + b**2 + c**2) 를 구하여라
## [링크](https://school.programmers.co.kr/learn/courses/30/lessons/181930?language=python3)

## 코드
    """ python3
    def solution(a, b, c):
        answer = 0
        if a != b and b != c and a != c:
            answer = a + b + c
        elif a == b == c:
            answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
        else:
            answer = (a + b + c) * (a**2 + b**2 + c**2)
        return answer
    """
## 요점
코드는 순서대로 처리하기 때문에 a != b != c 라고 조건을 지정하면 a 와 b 가 다르고 b 와 c가 다르다는 조건이 되어 a = 1, b = 2, c = 1 과 같은 경우 계산에 오류가 발생하여 무조건 a != b, b != c, c != a 로 모두 연결지어주어야한다.

set으로 순서와 중복을 없애 그 갯수가 1,2 그 외 로 구분지어 만들 수 있다.