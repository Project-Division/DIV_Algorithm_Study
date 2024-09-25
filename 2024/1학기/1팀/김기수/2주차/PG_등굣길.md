## 프로그래머스 - 등굣길

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/42898)

<br>

- ## 풀이
    - #### 오른쪽, 아래로만 움직일 수 있으므로 한 지점에서 목적지까지 갈 수 있는 방법의 수는 정해져있다.
    - #### 메모이제이션 기법을 통해 한 지점에서 목적지까지 갈 수 있는 방법을 알아냈을 때 테이블에 기록해두고, 이미 기록되어있는 지점에서는 탐색하지 않고 저장된 값을 바로 리턴하였다.

<br>

- ## 코드
    ```python
    from collections import deque

    def is_valid_pos(m, n, x, y):
        if 0 <= y < n and 0 <= x < m:
            return True
        return False

    table = None
    puddles_set = None

    def solve(m, n, cx, cy):
        global table, puddles_set
        
        if table[cy][cx] != -1:
            return table[cy][cx]
        if cx == m - 1 and cy == n - 1:
            return 1
        
        curr_result = 0
        for ox, oy in [(1, 0), (0, 1)]:
            nx, ny = (cx + ox, cy + oy)
            if is_valid_pos(m, n, nx, ny) and ((nx, ny) not in puddles_set):
                curr_result += solve(m, n, nx, ny)
        table[cy][cx] = curr_result
        return curr_result     

    def solution(m, n, puddles):
        global table, puddles_set
        table = [[-1 for _ in range(m)] for _ in range(n)]
        
        puddles_set = set()
        for px, py in puddles:
            puddles_set.add((px - 1, py - 1))
        
        solve(m, n, 0, 0)
        return table[0][0] % 1000000007
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/050067f1-dad9-4dda-8566-8529032cad3f)