# 프로그래머스 - 연속 펄스 부분수열의 합

- ## 문제
    - ## [링크](https://school.programmers.co.kr/learn/courses/30/lessons/161988)

<br>

- ## 풀이
    - #### 연속 부분수열의 최대합을 구하는 함수를 작성
    - #### 주어진 수열에 [-1, 1, -1, 1, ...] 을 곱한 수열과 [1, -1, 1, -1, ...]을 곱한 수열의 최대합 중 큰 값을 리턴

<br>

- ## 코드
    ```python
    # 연속 부분수열 최대값 구하는 함수
    def get_partial_max_sum(sequence):
        n = len(sequence)
        
        include_me = [0 for _ in range(n)]
        include_me[0] = sequence[0]
        exclude_me = [0 for _ in range(n)]
        include_me[0] = 0
        
        for i in range(n):
            # 나를 포함하여 부분수열을 완성하는 경우
            # 1. 직전것 포함하여 최대값 만든 경우 + 현재 포함
            # 2. 현재것만 선택
            include_me[i] = max(include_me[i - 1] + sequence[i], sequence[i])
            
            # 나를 포함하지 않고 부분수열을 완성하는 경우
            # 1. 직전까지만 포함한 최대값
            # 2. 직전것 포함하지 않은 지금까지의 최대값
            exclude_me[i] = max(include_me[i - 1], exclude_me[i - 1])
            
        # 마지막 항목에서의 둘 중 최대값이 연속 부분 수열의 최대합
        return max(include_me[n - 1], exclude_me[n - 1])

    def solution(sequence):
        n = len(sequence)
        answer = 0
        
        # [1, -1, 1, -1, ...]
        new_seq = sequence[:]
        curr_mult = 1
        for i in range(n):
            new_seq[i] *= curr_mult
            curr_mult = -1 if curr_mult == 1 else 1
        answer = max(answer, get_partial_max_sum(new_seq))
            
        # [-1, 1, -1, 1, ...]
        new_seq = sequence[:]
        curr_mult = -1
        for i in range(n):
            new_seq[i] *= curr_mult
            curr_mult = -1 if curr_mult == 1 else 1
        answer = max(answer, get_partial_max_sum(new_seq))
        
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/e350bf96-2f89-4b66-8632-ba8d4c59eaa9)
