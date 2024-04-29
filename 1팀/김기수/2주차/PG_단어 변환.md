# 프로그래머스 - 단어 변환

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/43163)

<br>

- ## 풀이
    - #### 최소 횟수를 찾는 것이므로 BFS 탐색을 사용했다.
    - #### words의 단어 중 현재 단어와 1글자만 차이나는 단어만 큐에 횟수를 추가하여 담았다.
    - #### answer를 0으로 초기화하여 target에 도달하지 못할 시 0을 리턴하였다.

<br>

- ## 코드
    ```python
    from collections import deque

    def get_diff_count(w1, w2):
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
        return count

    def solution(begin, target, words):
        answer = 0
        q = deque()
        visited = set()
        
        q.append((begin, 0))
        while len(q) > 0:
            cw, cc = q.popleft()
            
            for word in words:
                if word in visited:
                    continue
                
                diff = get_diff_count(cw, word)
                if diff == 1:
                    if word == target:
                        answer = cc + 1
                        return answer
                    else:
                        visited.add(word)
                        q.append((word, cc + 1))
        
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/f75b6c37-fb26-4ad6-b6a6-dff2ef499b75)
