# 프로그래머스 - 경주로 건설

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/67259#)

<br>

- ## 풀이
    - #### 최단거리를 구해야하므로 BFS 사용
    - <h4 style="color: red; font-weight: bold;">3차원 테이블 사용</h4>
      
        - <h4 style="color: red; font-weight: bold;">현재 위치까지는 최소 비용이 아니었어도, 현재 바라보고 있는 방향에 따라 최종 도착지에서의 비용은 최소 비용일 수 있으므로 방향에 따라 최소값을 따로 저장하여 관리하여야 함</h4>

<br>

- ## 코드
    ```python
    from collections import deque

    def solve(n, board, table):    
        turn_dict = {}
        turn_dict["vert"] = "horz"
        turn_dict["horz"] = "vert"

        dir_to_index = {}
        dir_to_index["vert"] = 0
        dir_to_index["horz"] = 1
        
        queue = deque()
        queue.append(((0, 0), 0, ""))
        while len(queue) > 0:
            pos, curr_cost, last_dir = queue.popleft()

            cy, cx = pos
            for oy, ox, ndir in [(1, 0, "vert"), (0, 1, "horz"), (-1, 0, "vert"), (0, -1, "horz")]:        
                ny, nx = cy + oy, cx + ox

                dir_index = dir_to_index[ndir] # 방향에 따른 테이블의 인덱스 구하기

                if not (0 <= ny < n and 0 <= nx < n):
                    continue

                if board[ny][nx] == 1:
                    continue

                if last_dir == ndir or last_dir == "": # 직선일 경우
                    next_cost = curr_cost + 100 # 직선도로 설치
                    if table[ny][nx][dir_index] < next_cost: 
                        continue

                    table[ny][nx][dir_index] = next_cost
                    queue.append(((ny, nx), next_cost, ndir))
                else: # 코너일 경우
                    next_cost = curr_cost + 500 + 100 # 직선도로, 코너 설치
                    if table[ny][nx][dir_index] < next_cost:
                        continue

                    table[ny][nx][dir_index] = next_cost
                    queue.append(((ny, nx), next_cost, ndir))

    def solution(board):
        n = len(board[0])
        
        MAX_COST = 700 * (n * n)
        table = [[[MAX_COST, MAX_COST] for _ in range(n)] for _ in range(n)] # 현재까지는 최소가 아니더라도 최종 도착 시 바라보고 있는 방향에 따라 최소일 수 있으므로 방향마다 최소값 따로 관리
        table[0][0][0] = 0
        table[0][0][1] = 0
        
        solve(n, board, table)
        
        answer = min(table[n - 1][n - 1]) # 최종 도착지에서의 두 방향으로 도착한 비용 중 최소 비용을 리턴
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/39f36653-1e9a-4991-99f6-c8183717682c)