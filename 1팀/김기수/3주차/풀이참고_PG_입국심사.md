# 프로그래머스 - 입국심사

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/43238)

<br>

- ## 정답
    - ### 이분탐색 이용
        - ### 주어지는 시간을 MID, 최소값을 1, 최대값을 가장 느린 심사관이 모두를 처리하는 ```10^9 * 인원 수```로 설정
        - ### 주어지는 시간 내 각 심사관들이 처리할 수 있는 인원 수
            ### ```주어진 시간 / 각 심사관들이 한 명을 처리하는 데 소요되는 시간```
        - ### 모든 심사관들이 처리할 수 있는 인원수가 n보다 크면 시간 줄이기 + 현재 시간값 기록 해두기
        - ### 모든 심사관들이 처리할 수 있는 인원수가 n보다 작으면 시간 늘리기

    - ### 코드
    ```python
    def solution(n, times):
    answer = 0
    left, right = (1, 1000000000 * n)
    while (left <= right):
        mid = (left + right) // 2

        curr_poss = 0
        for time in times:
            curr_poss += mid // time

        # print(left, right, mid, curr_poss)

        if curr_poss >= n:
            right = mid - 1
            answer = mid
        elif curr_poss < n:
            left = mid + 1
    return answer
    ```

<br>

- ## 오답
    - ### 최소힙을 사용해서 ```예상 종료 시간이 가장 빠른것만을 선택```하면서 n명을 전부 처리하는 식으로 하였을때 시간이 초과되었다.

    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/ebe1dacc-f437-444a-8747-ad7a68b7b83b)


    ```python
    import heapq

    def solution(n, times):
        times = sorted(times, reverse=True)
        
        h = []
        for _ in range(n - 1):
            # print(h)
            
            next_end, curr_end, dur = (-1, -1, -1)
            if len(h) > 0:
                next_end, curr_end, dur = heapq.heappop(h)
            
            if len(times) > 0:
                l_dur = times.pop()
                
                if next_end > 0:
                    if next_end > l_dur:
                        heapq.heappush(h, (l_dur + l_dur, l_dur, l_dur))
                        heapq.heappush(h, (next_end, curr_end, dur))
                    else:
                        heapq.heappush(h, (l_dur, 0, l_dur))
                        heapq.heappush(h, (curr_end + dur + dur, curr_end + dur, dur))
                else:
                    heapq.heappush(h, (l_dur + l_dur, l_dur, l_dur))
                continue
            
            heapq.heappush(h, (curr_end + dur + dur, curr_end + dur, dur))
                
        answer = heapq.heappop(h)[0]
        return answer
    ```

    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/e3c5f85b-d6fc-4880-a293-9badd4d8ed38)