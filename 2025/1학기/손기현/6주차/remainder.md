# 문제  
## 주어진 숫자의 각 자리 수 합을 9로 나누면 9를 나눈 나머지의 값이 같다.이 방법을 이용하여 입력 값의 나머지를 구하여라

## [링크](https://school.programmers.co.kr/learn/courses/30/lessons/181914)
## 코드
    """ python3
    def solution(number):
        spt_num = list(map(int, number))
        answer = 0
        for i in range(len(spt_num)):
            answer += spt_num[i]  
        return answer % 9


    """
## 요점
map으로 number 하나하나를 가지고 리스트화하여 개수만큼 반복해 더하고 9를 나누어서 값을 구했는데,
sum(map())으로 어짜피 더할 값을 리스트화 시키지않고 더하여 더 간단하게 구할 수 있다.