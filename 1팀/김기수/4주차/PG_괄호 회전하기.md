# 프로그래머스 - 괄호 회전하기

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/76502)

<br>

- ## 풀이
    - #### 스택을 사용하여 현재 문자열 괄호가 올바르게 되어 있는지 확인
    - #### 왼쪽으로 한번씩 회전한 문자열 괄호가 올바르면 결과값에 1 더함

<br>

- ## 코드
    ```python
    opener = {}
    opener["]"] = "["
    opener[")"] = "("
    opener["}"] = "{"

    def check_valid(s):
        global opener
        
        stack = []
        for i in s:
            if i in opener.values(): # 괄호 여는 문자이면
                stack.append(i) # 스택에 추가
            elif i in opener.keys(): # 괄호 닫는 문자이면
                if len(stack) <= 0: # 스택에 들어있는게 없을 경우 올바른 괄호 아님
                    return False
                if stack[-1] == opener[i]: # 스택 top이 괄호 여는 문자이면
                    stack.pop() # 스택에서 괄호 빼기
                else:
                    return False # 아니면 올바른 괄호 아님
        if len(stack) > 0: # 스택이 비어있지 않으면 올바른 괄호 아님
            return False
        return True

    def solution(s):
        answer = 0
        
        for i in range(len(s)):
            s = s[1:] + s[0] # 문자열 왼쪽으로 회전
            if check_valid(s):
                answer += 1
        return answer
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/28ffa1a3-a1a1-4184-974d-e103f9afaf19)