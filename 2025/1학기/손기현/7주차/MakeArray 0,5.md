# 문제  
## l, r 사이의 0,5로만 이루어진 리스트를 리턴하는데, 비었다면 -1 리턴하여라
## [링크](https://school.programmers.co.kr/learn/courses/30/lessons/181921)
## 코드
    """ python3
    def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if not set(str(i)) - set({'0','5'}):
            answer.append(i)
            
    if not answer:
        return [-1]
    else:
        return answer


    """
## 요점
r 값까지 반복하는데 set으로 중복값을 지우고 0, 5를 빼서 비었다면 answer에 추가한다.
answer이 비었다면 [-1]을 리턴하고 아니면 answer을 리턴하여 완성할 수 있었다.
