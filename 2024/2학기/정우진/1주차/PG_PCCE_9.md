# 프로그래머스 - PCCE 기출문제 9번 이웃한 

- ## 문제
    ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/250125)



<br>

- ## 오답


- ## 풀이


<br>


- ## 정답


   - ### 코드
    ```python
    def solution(board, h, w):
    answer= 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    color = board[h][w]
    for i in range(len(dh)):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if 0<= h_check < len(board) and 0<= w_check < len(board):
            if board[h_check][w_check] == color:
                answer += 1
    return answer
