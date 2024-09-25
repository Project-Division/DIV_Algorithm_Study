# 프로그래머스 _ 카펫

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/42842)

<br>

- ## 풀이
    - #### 완전탐색

<br>

- ## 코드
    ```python
    def solution(brown, yellow):
    # 전체 격자 개수
    carpet = brown + yellow
    
    # 전체 격자 개수부터 1까지 역순으로 탐색
    for i in range(carpet, 1, -1):
        # 나누어 떨어질 경우
        if carpet % i == 0:
            j = carpet / i
            
            # 테두리 1줄은 갈색 -> (가로 길이 - 2) * (세로 길이 - 2)
            if (i - 2) * (j - 2) == yellow: 
                return [i, j]
    ```
