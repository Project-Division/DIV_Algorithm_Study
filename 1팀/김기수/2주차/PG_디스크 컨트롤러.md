# 프로그래머스 - 디스크 컨트롤러

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/42627?language=python3)

<br>

- ## 설계
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/f38d1918-08c1-4958-aef8-20c1ad723625)

<br>

- ## 풀이
    - #### 각 시간별로 큐에 들어가있는 작업 중 최소 소요시간인 것을 선택하여 실행하도록 작성했다.
        - #### 운영체제 시간에 배운 SJF랑 유사한 로직인것같다.
    - #### 실행이 언제 끝날지 확신할 수 없어 for문을 0부터 10^6-1까지 돌렸더니 시간은 오래 걸렸지만 전부 정답처리가 되긴 했다.

<br>

- ## 코드
    ```python
    import heapq

    def solution(jobs):
        job_dict = {}
        for s, dur in jobs:
            if s in job_dict:
                job_dict[s].append((s, dur))
            else:
                job_dict[s] = [(s, dur)]
        
        h = []
        answer = 0
        curr_start, curr_remain = (-1, 1)
        is_processing = False
        for time in range(0, 1000*1000):
            if time in job_dict:
                for s, dur in job_dict[time]:
                    heapq.heappush(h, (dur, s))
                    
            curr_remain -= 1
            if curr_remain <= 0:
                if is_processing:
                    answer += (time - curr_start)
                    curr_remain = 0
                    is_processing = False
                if len(h) > 0:
                    curr_remain, curr_start = heapq.heappop(h)
                    is_processing = True
                    # print(time, curr_start, curr_remain, answer)
        
    return answer // len(jobs)
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/4c60f993-23bc-4952-9ab8-b2a82d84fbab)