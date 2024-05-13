# 프로그래머스 - N으로 표현

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/42895#)

<br>

- ## 풀이
    - #### BFS 탐색, 메모이제이션 이용

    - #### 현재 수를 만드는 데 소요된 횟수와, 만들어진 수를 큐에 저장

    - #### 현재까지 만들어진 수에 N, NN, NNN, NNNN... 을 사칙 연산하여 나온 결과가 현재까지 나왔던 횟수보다 적을 시, 테이블 업데이트

    - #### 횟수가 8을 초과하기 전까지 업데이트된 table[number]의 value가 정답인 최소 횟수이다.

<br>

- ## 코드
    ```python
    from collections import deque

    def solution(N, number):
        queue = deque()
        table = {}
        table[0] = 0
        
        queue.append((0, 0))
        while len(queue) > 0:
            count, cn = queue.popleft()
            if count > 8:
                continue
            
            for nc in range(1, 9 - count):
                nn = int(str(N) * nc)
                # print(cn, nn)
            
                for next in [cn + nn, cn - nn, cn * nn, cn // nn]:
                    if next in table:
                        if table[next] >= count + nc:
                            table[next] = min(table[next], count + nc)
                            queue.append((count + nc, next))
                    else:
                        table[next] = count + nc         
                        queue.append((count + nc, next))
        
        answer = -1
        if number in table:
            answer = table[number]
            if answer > 8:
                answer = -1
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/874bc288-f9b0-40f0-8a25-8fcc0e12a135)
