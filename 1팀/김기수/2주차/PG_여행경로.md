# 프로그래머스 - 여행경로

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/43164#)

<br>

- ## 풀이
    - #### 주어진 티켓으로 갈 수 있는 모든 경우의 수를 다 찾은 다음 리스트를 오름차순으로 정렬하여 답을 출력하였다.

    - #### 이미 사용된 티켓을 다시 사용하는 경우를 필터링하기 위해 티켓을 [목적지, 사용여부] 형태로 저장하였다.

    - #### 이미 시도해본 경로를 다시 탐색하는 경우를 필터링하기 위해 시도해본 시퀀스를 visited에 저장해두고 이미 시도해본 시퀀스인 경우는 재시도하지 않도록 하였다.

<br>

- ## 코드
    ```python
    visited = set()

    results = []
    def dfs(graph, curr_node, root, max_root):
        global visited, results
        
        if len(root) == max_root:
            results.append(tuple(root))
            return True
        else:
            if (curr_node not in graph):
                return False
            
            for i, (next_node, count) in enumerate(graph[curr_node]):
                if count > 0:
                    continue
                    
                root.append(next_node)
                if tuple(root) in visited:
                    root.pop()
                    continue
                visited.add(tuple(root))
                
                graph[curr_node][i][1] = 1
                dfs(graph, next_node, root, max_root)
                graph[curr_node][i][1] = 0
                root.pop()

    def solution(tickets):
        global results
        
        graph = {}
        for start, dest in tickets:
            if start not in graph:
                graph[start] = [[dest, 0]]
            else:
                if dest not in graph[start]:
                    graph[start].append([dest, 0])
            
        dfs(graph, "ICN", ["ICN"], len(tickets) + 1)
        
        return sorted(results)[0]
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/399fc661-a524-4f86-81b0-9845ae0fb8c6)