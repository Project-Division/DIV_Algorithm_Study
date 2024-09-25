# 프로그래머스 - 폰켓몬

- ## 문제
    ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/1845)



<br>

- ## 오답


- ## 풀이


<br>


- ## 정답


   - ### 코드
    ```python

    def solution(nums):
    answer = len(set(nums))
    if answer > len(nums)/2:
        return len(nums)/2
    return answer
