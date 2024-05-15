# 백준 17433 _ 신비로운 수

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/12953?language=python3)

<br>

- ## 풀이
    - #### 최대공약수를 구하여 최소공배수를 구한다

<br>

- ## 코드
    ```python
    def solution(arr):
    res = 1
    for i in arr:
        res = lcm(res, i)
    return res
    
    # 최대공약수
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # 최소공배수
    def lcm(a, b):
        return a * b / gcd(a, b)
    ```