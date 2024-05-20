# 프로그래머스 - 풍선 터트리기

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/68646)

<br>

- ## 풀이
    - #### 현재 숫자를 남길 수 없는 경우
        - #### 양쪽에서 큰 값만을 터트려 온 숫자를 테이블에 기록
        - #### 현재 숫자와 양쪽에서 큰 값만을 터트려 온 숫자 비교
        - #### 현재 숫자와 비교했을 때 양쪽 모두보다 현재 숫자가 크면 2개 이상을 작은 숫자를 터트리게 되는 것이므로 남길 수 없게된다.

<br>

- ## 코드
    ```python
    def solution(a):
        min_table = [0 for _ in range(len(a))]
        min_table[0] = a[0]
        rev_min_table = [0 for _ in range(len(a))]
        rev_min_table[-1] = a[-1]
        
        for i in range(1, len(a)):
            min_table[i] = min(min_table[i - 1], a[i]) # 오른쪽 방향으로 i번째 까지 큰 풍선만을 터트렸을 때 남은 값
        for i in range(len(a) - 2, -1, -1):
            rev_min_table[i] = min(rev_min_table[i + 1], a[i]) # 왼쪽 방향으로 i번째 까지 큰 풍선만을 터트렸을 때 남은 값
        
        answer = min(2, len(a)) # 양쪽 끝은 항상 가능하므로 미리 정답에 저장해두기
        for i in range(1, len(a) - 1): # 양쪽 끝 제외 탐색
            bigger_count = 0
            if min_table[i - 1] < a[i]: # 왼쪽과 비교했을 때 더 작은 풍선을 터트려야 현재 풍선을 남길 수 있는 경우
                bigger_count += 1
            if rev_min_table[i + 1] < a[i]: # 오른쪽과 비교했을 때 더 작은 풍선을 터트려야 현재 풍선을 남길 수 있는 경우
                bigger_count += 1
            if bigger_count < 2: # 2번 미만으로 작은 풍선을 터트리는 경우 정답에 추가
                answer += 1
        
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/d167a971-c5c4-4623-9c49-a57cffa718dd)
