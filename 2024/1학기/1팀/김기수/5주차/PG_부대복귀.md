# 프로그래머스 - 부대복귀

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/132266)

<br>

- ## 풀이
    - #### Dijkstra 최단경로 알고리즘을 사용하여 출발지점을 destination으로 하는 다른 노드로의 최단 경로를 구함

<br>

- ## 코드
    ```python
    import heapq

    def solution(n, roads, sources, destination):
        MAX_DIST = n + 1
        
        road_dict = {}
        for i in range(1, n + 1):
            road_dict[i] = []
        for a, b in roads:
            road_dict[a].append(b)
            road_dict[b].append(a)
        
        min_dists = [MAX_DIST for _ in range(n + 1)]
        min_dists[destination] = 0
        h = []
        heapq.heappush(h, (0, destination))
        while (len(h) > 0):
            curr_dist, curr_node = heapq.heappop(h)
            
            for next_node in road_dict[curr_node]:
                next_dist = curr_dist + 1
                if min_dists[next_node] > next_dist:
                    heapq.heappush(h, (next_dist, next_node))
                    min_dists[next_node] = next_dist
        
        answer = []
        for src in sources:
            if min_dists[src] == MAX_DIST:
                answer.append(-1)
            else:
                answer.append(min_dists[src])
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/cead3252-3d0f-4168-a0ea-8c1c58c9e9e5)
