# 프로그래머스 - 섬 연결하기

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/42861)

<br>

- ## 풀이
    - #### 최소 비용 신장 트리 알고리즘 이용
        - #### 소요시간을 최대한 줄이기 위하여 간선 정보를 딕셔너리에 저장, min_dist를 구하는 방법으로 최소 힙 사용

<br>

- ## 코드
    ```python
    import heapq

    def solution(n, costs):
        answer = 0
        
        # 간선 정보 초기화
        costs_dict = {}
        for i in range(n):
            costs_dict[i] = []
        for a, b, cost in costs:
            costs_dict[a].append((b, cost))
            costs_dict[b].append((a, cost))
        
        visited = set()
        edge_count = 0
        min_dist = []
        
        # 시작 노드에서의 edge들로 min_dist 초기화
        start_node = 0
        for dest, cost in costs_dict[start_node]:
            heapq.heappush(min_dist, (cost, dest))
        visited.add(start_node)
            
        # n - 1개 간선이 선택될 때 까지 반복
        while (edge_count < n - 1):
            cost, dest = heapq.heappop(min_dist)
            if dest in visited:
                continue
            visited.add(dest)
            
            # 선택된 간선의 비용 정답에 더하기
            answer += cost
            edge_count += 1
            
            # 현재 노드에서의 간선 정보로 min_dist 변경
            for dest, cost in costs_dict[dest]:
                heapq.heappush(min_dist, (cost, dest))
        
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/0b9d1930-c373-4ce8-b24a-9282e9fa80e0)
