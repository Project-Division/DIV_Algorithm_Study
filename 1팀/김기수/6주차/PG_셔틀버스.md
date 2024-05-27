# 프로그래머스 - 셔틀버스

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/17678)

<br>

- ## 풀이
    - #### 크루 도착 시간 정보를 스택처럼 활용하기 위하여 역순으로 정렬 후 pop, append 메소드 사용

<br>

- ## 코드
    ```python
    def str_to_time(s): # 문자열 형태 시간을 정수로 변환
        t = list(map(int, s.split(":")))
        result = 0
        result += t[0] * 60
        result += t[1]
        return result

    def time_to_str(t): # 정수 형태 시간을 문자열 형태로 변환
        time = [0 for _ in range(2)]
        time[0] = t // 60
        time[1] = t % 60
        return ":".join(map(lambda x: str(x) if x >= 10 else "0"+str(x), time))

    def solution(n, t, m, timetable):
        timetable = map(str_to_time, timetable)
        timetable = sorted(timetable, reverse=True) # 크루 도착시간 역순정렬
        
        curr_bus_arrive = 0 # 마지막 버스 도착시간
        curr_p_count = 0 # 마지막 버스에 탑승한 크루 수
        curr_p_arrive = 0 # 마지막으로 버스에 탑승한 크루의 도착시간
        for bus_seq in range(n):
            curr_bus_arrive = str_to_time("09:00") + (t *  bus_seq) # 현재 버스 도착 시간
            
            curr_p_count = 0
            while True:
                if len(timetable) < 1: # 탑승할 수 있는 승객이 없는 경우 while 탈출
                    break
                
                curr_p_arrive = timetable.pop() # 가장 먼저 도착한 승객 한명
                if curr_bus_arrive >= curr_p_arrive: # 버스 도착 전에 온 승객이라면
                    curr_p_count += 1 # 태우기
                    if curr_p_count >= m: # 정원 초과 시
                        break # while 탈출
                else: # 버스 도착 후에 온 승객이라면
                    timetable.append(curr_p_arrive) # 다시 스택에 담아두고 while탈출
                    break
            
        if curr_p_count < m: # 마지막 버스에 탄 크루 수가 정원보다 적으면
            return time_to_str(curr_bus_arrive) # 버스 도착시간에 맞춰오는것이 최선
        return time_to_str(curr_p_arrive - 1) # 마지막 버스에 탄 크루 수가 정원과 같으면 마지막 한명보다는 1분 빨리 와야지 탈 수 있음
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/c24e4b23-117f-473c-889b-6db707fe68d2)
