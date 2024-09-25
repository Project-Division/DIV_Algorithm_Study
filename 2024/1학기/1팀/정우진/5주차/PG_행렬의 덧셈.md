# 프로그래머스 - 행렬의 덧셈

- ## 문제
    ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/12950)



<br>

- ## 오답


- ## 풀이


<br>


- ## 정답


   - ### 코드
    ```python
    def solution(arr1, arr2):
    answer = [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]
    return answer
