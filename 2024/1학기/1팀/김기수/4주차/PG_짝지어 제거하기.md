# 프로그래머스 - 짝지어 제거하기

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/12973#)

<br>

- ## 풀이
    - #### 문자열의 끝에서부터 스택에 한글자씩 넣으면서 스택 TOP의 2개가 같을 시 pop 2회하여 제거
    - #### 스택에 남은 문자가 없을 시 전부 제거된것으로 판단

<br>

- ## 코드
    ```python
    def solution(s):
        stack = []
        
        for i in range(len(s) - 1, -1, -1):
            stack.append(s[i])
            if len(stack) >= 2:
                if stack[-2] == stack[-1]:
                    stack.pop()
                    stack.pop()
        
        answer = 0
        if len(stack) == 0:
            answer = 1
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/1ec02c2e-8e94-43dc-90a0-5ee2f11bf364)
