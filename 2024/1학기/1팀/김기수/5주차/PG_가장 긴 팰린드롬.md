# 프로그래머스 - 가장 긴 팰린드롬

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/12904#)

<br>

- ## 풀이
    - ### 1 <= len(s) <= 2500
        - #### 완전 탐색으로는 최소 O(n^3)이 소요되므로 불가능하다.

    - ### 다이나믹 프로그래밍
        - #### 팰린드롬의 길이가 짝수일 때, 홀수일 때 각각 테이블 구성
        - #### table[중심점과 떨어진 거리][중심점의 위치] 테이블 사용
        - #### 각 끝문자가 같으면 현재 테이블의 값 = 이전 거리까지의 길이 + 2
        - #### 길이가 짝수 홀수일 때 각각의 최대값을 정답으로 사용

<br>

- ## 코드
    ```python
    def solution(s):
        answer = 0
        
        n = len(s)
        
        # 팰린드롬의 길이가 홀수인 경우
        table = [[0 for _ in range(n)] for _ in range(n)]
        for x in range(n):
            table[0][x] = 1 # 중심점 거리가 0(본인만 포함)인 모든 팰린드롬 길이 1로 초기화
        
        for x in range(1, n): # 중심점 위치
            for y in range(1, x + 1): # 중심점으로부터 떨어진 거리
                if table[y - 1][x] > 0:
                    if not (0 <= (x - y) < n and 0 <= (x + y) < n):
                        break                    
                    if s[x - y] == s[x + y]:
                        table[y][x] = table[y - 1][x] + 2
                    else:
                        break
                        
        for i in table:
            answer = max(answer, max(i))
                        
        # 팰린드롬의 길이가 짝수인 경우
        table = [[0 for _ in range(n)] for _ in range(n)]
        for x in range(len(s) - 1): # 중심점
            for y in range(1, x + 2): # 중심점으로부터 떨어진 거리
                left_cursor = x - y + 1
                right_cursor = x + y
                if not (0 <= left_cursor < n and 0 <= right_cursor < n):
                    break     
                if s[left_cursor] == s[right_cursor]:
                    table[y][x] = table[y - 1][x] + 2
                else:
                    break
                        
        # for i in table:
        #     print(i)
                            
        for i in table:
            answer = max(answer, max(i))

        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/d521a436-ab92-4d55-a897-a35600dab861)
