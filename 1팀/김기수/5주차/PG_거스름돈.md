# 프로그래머스 - 거스름돈

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/12907)

<br>

- ## 풀이
    - #### 거스름돈 n이 주어졌을 때 거스름돈으로 사용할 수 있는 동전 money를 사용하여 거스름돈 n을 만들 수 있는 경우의 수 구하기

    - #### 다이나믹 프로그래밍

    - #### 같은 조합은 1개의 경우로 취급함
        - #### 중복을 피하기 위해 table[y][x]를 money의 x번 동전까지 사용하여 y 금액을 만드는 경우의 수로 정의
        - #### x번 동전까지 사용하여 y 금액 만드는 경우의 수
            - #### x - 1번 동전까지 사용하여 y금액 만든 경우
            - #### x번 동전까지 사용하여 (y 금액 - x번 동전 금액) 만든 것에 x번 동전 추가하여 y금액 만든경우

<br>

- ## 코드
    ```python
    def solution(n, money):
        table = [[0 for _ in range(len(money))] for _ in range(n + 1)]
        for x in range(len(money)):
            table[0][x] = 1
        
        for x in range(len(money)): # x번 동전까지 사용
            for y in range(1, n + 1): # y금액 만들기
                curr_coin = money[x] # 현재 동전
                if y - curr_coin >= 0:
                    table[y][x] += table[y - curr_coin][x]
            
                if x >= 1:
                    table[y][x] += table[y][x - 1]
            
        
        answer = table[n][len(money) - 1]
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/5e6e8eda-9829-4da3-828d-e91c8a764c3e)