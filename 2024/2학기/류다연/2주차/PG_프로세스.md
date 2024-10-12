# 프로그래머스 _ 프로세스

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/42587)

<br>

- ## 코드
    ```python
    from collections import deque

    def solution(priorities, location):
        q = deque(priorities)
        answer = 0
        
        while q:
            M = max(q)
            l = q.popleft()
            location -= 1
            if M != l:
                q.append(l)
                if location < 0:
                    location = len(q) - 1
            else:
                answer += 1
                if location < 0:
                    break
        return answer
    ```