# 프로그래머스 - 가장 먼 노드

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/49189)

<br>

- ## 풀이
    - #### 최단경로 알고리즘
        - #### 노드의 개수가 최대 20,000개이므로 O(n^3)이 소요되는 Bellman-Ford로는 해결이 불가능하다.
        - #### Dijkstra 알고리즘을 사용

    - #### 시간을 최대한 절약하기 위해 min_dist를 찾는 방식으로 힙을 사용
    - #### 노드간 연결 여부를 매번 n번 탐색하지 않기 위해 보유한 간선 만큼만 탐색하도록 하였다.


<br>

- ## 코드
    ```python
    import heapq

    def solution(n, edge):
        MAX_DIST = n
        
        vertex = {}
        for i in range(1, n + 1):
            vertex[i] = []
        for a, b in edge:
            vertex[a].append(b)
            vertex[b].append(a)
        
        h = []
        dists = [MAX_DIST for _ in range(n + 1)]
        dists[1] = 0
        visited = [0 for _ in range(n + 1)]
        
        max_dist = 0
        heapq.heappush(h, (0, 1))
        while (len(h) > 0):
            dist, node = heapq.heappop(h)
            
            for i in vertex[node]:
                next_dist = dist + 1
                if dists[i] > next_dist and visited[i] == 0:
                    visited[i] = 1
                    heapq.heappush(h, (next_dist, i))
                    dists[i] = next_dist
                    max_dist = max(max_dist, next_dist)
        
        answer = len([i for i in dists if i == max_dist])
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/62a8cf3e-1286-44d5-bcd6-703a260c5cef)