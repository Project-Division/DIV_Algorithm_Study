# 프로그래머스 PCCP 기출문제 1

- ## 문제
    ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/340213)

    당신은 동영상 재생기를 만들고 있습니다. 당신의 동영상 재생기는 10초 전으로 이동, 10초 후로 이동, 오프닝 건너뛰기 3가지 기능을 지원합니다. 각 기능이 수행하는 작업은 다음과 같습니다.

    10초 전으로 이동: 사용자가 "prev" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 전으로 이동합니다. 현재 위치가 10초 미만인 경우 영상의 처음 위치로 이동합니다. 영상의 처음 위치는 0분 0초입니다.
  
    10초 후로 이동: 사용자가 "next" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 후로 이동합니다. 동영상의 남은 시간이 10초 미만일 경우 영상의 마지막 위치로 이동합니다. 영상의 마지막 위치는 동영상의 길이와 같습니다.
  
    오프닝 건너뛰기: 현재 재생 위치가 오프닝 구간(op_start ≤ 현재 재생 위치 ≤ op_end)인 경우 자동으로 오프닝이 끝나는 위치로 이동합니다.
  
    동영상의 길이를 나타내는 문자열 video_len, 기능이 수행되기 직전의 재생위치를 나타내는 문자열 pos, 오프닝 시작 시각을 나타내는 문자열 op_start, 오프닝이 끝나는 시각을 나타내는 문자열 op_end, 사용자의 입력을 나타내는 1차원 문자열 배열 commands가 매개변수로 주어집니다. 이때 사용자의 입력이 모두 끝난 후 동영상의 위치를 "mm:ss" 형식으로 return 하도록 solution 함수를 완성해 주세요.
 
<br>

- ## 오답

    - 먼저 현재 위치가 오프닝 구간 안에 있는지 확인한다.
        - 오프닝 구간에 있다면 오프닝 끝으로 이동해 이동하기 기능을 적용했다.
        - 오프닝 구간에 없다면 이동하기 기능을 적용 후 다시 오프닝 구간에 있는지 확인했다.
    - 하지만 예제 3개 중 1개만 실행되었고.. 여러번 고쳤지만 해결할 수 없었다.. ㅜㅜ

    - 코드
  
        ```python
        def solution(video_len, pos, op_start, op_end, commands):
        answer = ''
        
        pos_mm, pos_ss = map(int, pos.split(":"))
        video_len_mm, video_len_ss = map(int, video_len.split(":"))
        op_start_mm, op_start_ss = map(int, op_start.split(":"))
        op_end_mm, op_end_ss = map(int, op_end.split(":"))
        
        if ((op_start_mm <= pos_mm < op_end_mm) and (op_start_ss <= pos_ss <= op_end_ss)) or ((pos_mm == op_end_mm) and (pos_ss < op_end_ss)):
            pos_mm = op_end_mm
            pos_ss = op_end_ss
            
            for move in commands:
                if move == "prev":
                    # 00분
                    if pos_mm == 0:
                        pos_mm = 0
                        if pos_ss <= 10:
                            pos_ss = 0
                        else:
                            pos_ss = pos_ss - 10
                    # 01분 이상
                    else:
                        pos_mm = pos_mm - 1
                        if pos_ss <= 10:
                            pos_ss = 60 + (pos_ss - 10)
                        else:
                            pos_ss = pos_ss - 10
                if move == "next":
                    if (pos_ss + 10) >= 60:
                        pos_mm = pos_mm + 1
                        pos_ss = (pos_ss + 10) - 60
                    else:
                        pos_mm = pos_mm
                        pos_ss = pos_ss + 10
                        
                if ((op_start_mm <= pos_mm < op_end_mm) and (op_start_ss <= pos_ss <= op_end_ss)) or ((pos_mm == op_end_mm) and (pos_ss < op_end_ss)):
                    pos_mm = op_end_mm
                    pos_ss = op_end_ss
        
        return str(pos_mm).zfill(2)+":"+str(pos_ss).zfill(2)
        ```

<br>

- ## 정답

    - chat gpt의 도움을 받아 모든 분과 초를 초로 바꾸어 계산하는 것이 낫다는 것을 알게 되었고 나머지 과정은 같았다.
    - 최종 결과(초)를 분과 초로 다시 바꾸어 출력하였다.
    - 근데 또 결과가 다르게 나왔고 prev와 next에서 min, max 함수를 사용하는 것이 낫다는 것을 또 알게되었다.
 
    - 코드
  
      ```python
        def solution(video_len, pos, op_start, op_end, commands):
        answer = ''
        
        pos_mm, pos_ss = map(int, pos.split(":"))
        video_len_mm, video_len_ss = map(int, video_len.split(":"))
        op_start_mm, op_start_ss = map(int, op_start.split(":"))
        op_end_mm, op_end_ss = map(int, op_end.split(":"))
        
        # 현재 위치를 총 초로 변환
        pos_total = pos_mm * 60 + pos_ss
        video_len_total = video_len_mm * 60 + video_len_ss
        op_start_total = op_start_mm * 60 + op_start_ss
        op_end_total = op_end_mm * 60 + op_end_ss
        
        # 처음 시작할 때 위치가 오프닝 시간에 있을 때 스킵
        if op_start_total <= pos_total <= op_end_total:
            pos_total = op_end_total
        
        for move in commands:
            if move == "prev":
                pos_total = max(0, pos_total - 10)
            elif move == "next":
                pos_total = min(video_len_total, pos_total + 10)
    
            # 이동 후에도 오프닝 구간에 있으면 오프닝 끝으로 이동
            if op_start_total <= pos_total <= op_end_total:
                pos_total = op_end_total
                
        # 최종 결과를 분과 초로 변환        
        pos_mm = pos_total // 60
        pos_ss = pos_total % 60
        
        return str(pos_mm).zfill(2)+":"+str(pos_ss).zfill(2)
        ```

<br>

- ## 결과
    - 궁금해서 풀어보았으나 현재 나의 실력으로는 부족하다는 것을 깨달았고 할 수 있는 단계부터 다시 시작하기로 다짐함..

    ![pg_PCCP_01 결과](https://github.com/user-attachments/assets/256f0ff5-7611-45fc-b5ea-fa98bd69e7ab)
