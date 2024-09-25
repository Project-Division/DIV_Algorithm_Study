# 프로그래머스 - 기지국 설치

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/12979)

<br>

- ## 풀이
    - #### 1 <= 아파트 수 <= $ 2 * 10 ^ 8 $
        - #### $ O(n) $ 시간초과

    - #### 1 <= 기지국 수, 기지국의 범위 <= $ 10 ^ 5 $
        - #### $ O(n) $ 가능
            - #### 기지국을 기준으로 계산하여야 시간내에 해결 가능

    <br>

    - ### 로직
        - #### 현재 위치를 가장 오른쪽 아파트로 설정

        <br>

        - #### 가장 오른쪽에 있는 기지국 꺼내기
        - #### 현재 위치와 꺼낸 기지국의 오른쪽 끝 전파 도달 거리 사이에 설치해야하는 최소 기지국 수 구하여 정답에 더하기
        - #### 현재 위치를 현재 기지국의 왼쪽 끝 전파 도달 거리로 변경

        <br>

        - #### 마지막에 가장 왼쪽에 남은 아파트들에 설치해야하는 최소 기지국 수 구하여 정답에 더하기

<br>

- ## 코드
    ```python
    def get_region_station(end, start, w): # start ~ end까지 설치해야 하는 최소 기지국 수
        div = (end - start + 1) // (w * 2 + 1)
        result = div
        
        mod = (end - start + 1) % (w * 2 + 1)
        if mod > 0:
            result += 1
        
        return result
        
    def solution(n, stations, w):
        answer = 0

        cursor = n # 가장 끝 아파트를 첫 위치로 설정
        while len(stations) > 0 and cursor > 0:
            curr_station = stations.pop() # 오른쪽 끝 기지국 꺼내기
            
            answer += get_region_station(cursor, curr_station + w + 1, w) # 오른쪽 끝 기지국의 오른쪽 전파 도달 범위 ~ 현 위치 사이 기지국 수
            
            cursor = curr_station - w - 1 # 현위치를 기지국의 왼쪽 전파 도달 범위로 설정
            
        answer += get_region_station(cursor, 1, w) # 마지막 왼쪽 끝의 아파트들을 위한 기지국 수
        
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/86c7531c-efad-4f1a-8ae7-24089f1edd99)
