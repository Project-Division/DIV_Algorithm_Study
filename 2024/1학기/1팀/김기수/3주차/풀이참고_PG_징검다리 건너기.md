# 프로그래머스 - 징검다리 건너기

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/64062)

- ## 풀이
    - #### stones 배열의 크기는 1 이상 200,000 이하입니다.

    - #### stones 배열 각 원소들의 값은 1 이상 200,000,000 이하인 자연수입니다.
        - #### 모든 stones 원소를 1씩 감소시켜가며 0이 된 징검다리 수가 연속 K개를 넘지 않는 최대값을 찾는 것은 시간 초과된다.

        - #### 이분 탐색을 이용하여 지나갈 수 있는 인원의 최대값을 구한다.
            - #### 초기 LEFT: 1, RIGHT: 2 * (10 ^ 6)
            - #### 징검다리 전체에서 현재 MID값을 뺐을 때 연속 0이 K개 이하: 더 늘려도 됨
                - #### LEFT를 MID + 1로 변경
                - #### LEFT가 RIGHT보다 커지면 LEFT를 반환
            - #### 연속 0이 K개 이상: 더 줄여야 함
                - #### RIGHT를 MID - 1로 변경

    - #### 시간 복잡도
        - #### 각 MID마다 연속된 0 개수 세기 = O(len(stones))
        - #### 이분탐색 = O(log(2*(10^6)))
        - #### O(len(stones) * O(log(2*(10^6))))

- ## 코드
    ```python
    def get_max_continuous(stones, sub, k):
    cont = 0
    for i in range(len(stones)):
        sub_val = stones[i] - sub
        if sub_val <= 0:
            cont += 1
            if cont >= k:
                return cont
        else:
            cont = 0
    return cont

    def solve(stones, k, left, right):
        if left > right:
            return left
        
        mid = (left + right) // 2      
        
        cont = get_max_continuous(stones, mid, k)
        if cont < k:
            next_left, next_right = (mid + 1, right)
            return solve(stones, k, next_left, next_right)
        else:
            next_left, next_right = (left, mid - 1)
            return solve(stones, k, next_left, next_right)

    def solution(stones, k):
        return solve(stones, k, 1, 200000000)   
    ```