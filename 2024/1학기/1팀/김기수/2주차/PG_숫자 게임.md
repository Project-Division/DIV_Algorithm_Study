# 프로그래머스 - 숫자 게임

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/12987)

<br>

- ## 설계
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/ba00ab2c-a0be-475d-9c91-3e0cc0480ffe)

<br>

- ## 코드
    ```python
    import heapq

    def solution(A, B):
        answer = 0
        
        heap = []
        
        A = sorted(A, reverse=True)
        for i in B:
            heapq.heappush(heap, -i)
            
        for i in range(len(A)):
            curr_b = -1 * heapq.heappop(heap)
            if curr_b > A[i]:
                answer += 1
            else:
                heapq.heappush(heap, -curr_b)

        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/542a322a-d53f-4815-818b-d38892aafa33)