# 프로그래머스 - 행렬의 곱셈

- ## 문제
    ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/10814)



<br>

- ## 오답


- ## 풀이


<br>


- ## 정답


   - ### 코드
    ```python
    def solution(arr1, arr2):
        
        answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
        
        for i in range(len(arr1)):
            lists=[]
            for j in range(len(arr2[0])):
                for k in range(len(arr1[0])):
                    answer[i][j] += arr1[i][k] * arr2[k][j]
        
        return answer
