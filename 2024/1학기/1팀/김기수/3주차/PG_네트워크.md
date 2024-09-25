# 프로그래머스 - 네트워크

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)

- ## 풀이
    - #### 방문하지 않은 컴퓨터 중 연결되어 있는 컴퓨터가 있으면 방문 후 방문 처리
    - #### 본인 포함해서 방문할 수 있는 컴퓨터가 한 대라도 있으면 결과값에 +1

- ## 코드
    ```python
    visited = set()

    def search(computers, n, computer):
        global visited
        
        result = False
        for i in range(n):
            if computers[computer][i] == 1:
                if i not in visited:
                    result = True
                    visited.add(i)
                    search(computers, n, i)
        return result

    def solution(n, computers):
        answer = 0
        for i in range(n):
            if search(computers, n, i):
                answer += 1
                    
        return answer
    ```