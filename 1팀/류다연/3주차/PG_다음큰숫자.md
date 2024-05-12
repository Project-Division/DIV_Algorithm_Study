# 프로그래머스 _ 다음 큰 숫자

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/12911)

<br>

- ## 코드
    ```python
    def solution(n):
    nxt = n+1
    while True:
        if bin(n)[2:].count("1") == bin(nxt)[2:].count("1"):
            return nxt
        nxt += 1
    ```
