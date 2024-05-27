# 프로그래머스 - 같은 숫자는 싫어

- ## 문제
    ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/12906)



<br>

- ## 오답


- ## 풀이


<br>


- ## 정답


   - ### 코드
    ```python

    def solution(arr):
        ans = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                ans.append(arr[i])
        return ans
