# 프로그래머스 _ 달리기 경주

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/178871)

<br>

- ## 코드
    ```python
    def solution(players, callings):
        result = {player: i for i, player in enumerate(players)}
        for who in callings:
            idx = result[who] 
            result[who] -= 1 
            result[players[idx-1]] += 1 
            players[idx-1], players[idx] = players[idx], players[idx-1]
        return players
    ```