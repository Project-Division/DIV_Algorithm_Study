# 프로그래머스 - 최고의 집합

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/12938)

<br>

- ## 설계
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/b547ff71-aa54-4ad3-8ef8-211c696a353f)

<br>

- ## 코드
    ```python
    def solution(n, s):
        if n > s: return [-1]

        answer = []
        curr_s = s
        for i in range(n, 0, -1):
            curr_val = curr_s // i
            answer.append(curr_val)
            curr_s -= curr_val
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/dbcbc8d0-2c0a-4d87-8c73-9cf6248289fc)