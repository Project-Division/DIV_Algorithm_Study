# 프로그래머스 - 홀수 vs 짝수

- ## 문제
    [링크](https://school.programmers.co.kr/learn/courses/30/lessons/181887)

- ## 코드
    ```python
    def solution(num_list):
        a,b = 0,0
        for i in range(len(num_list)):
            if i % 2 == 0:
                a += num_list[i]
            else:
                b += num_list[i]
        if a > b:
            return a
        else:
            return b
        return answer
    ```