# 프로그래머스 - 순위

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/49191?language=python3)

<br>

- ## 풀이
    - #### 순위를 정확히 알 수 있는 사람은 (이긴 사람 수 + 진 사람 수 = 전체 인원수 - 1)인 사람들이다.
        - #### 1. 방향성 그래프를 이용하여 진사람이 이긴 사람을 가리키도록 테이블을 구성한다.
        - #### 2. 진 사람 방향에서 이긴 사람 방향으로 DFS 탐색하면서 본인보다 윗 순위에 있는 사람 수와 본인보다 아랫순위에 있는 사람 수를 합해서 counts 테이블에 저장한다.
        - #### 3. counts 테이블의 값이 n - 1인 사람의 수를 구하여 출력하였다.

<br>

- ## 코드
    ```python
    counts = None

    search_count = 0
    def search(matrix, n, curr, visited):
        global counts, search_count
        
        for i in range(n + 1):
            if matrix[curr][i] != -1 and visited[i] == 0:
                counts[i] += 1 # 본인 하위 노드 개수
                search_count += 1
                visited[i] = 1
                search(matrix, n, i, visited)

    def solution(n, results):
        global counts, search_count
        
        counts = [0 for _ in range(n + 1)]
        matrix = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        for win, lose in results:
            matrix[lose][win] = 0

        for i in range(1, n + 1):
            search_count = 0
            search(matrix, n, i, [0 for _ in range(n + 1)])
            counts[i] += search_count # 본인 상위 노드 개수

        # for i in matrix[1:]:
        #     print(i[1:])
        # print(counts[1:])
        
        answer = len([i for i in counts if i == n - 1])
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/67bff5ab-ab9b-4c1f-9872-77fb8b700f61)