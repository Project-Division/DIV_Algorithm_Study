# 프로그래머스 _ 올바른 괄호

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/12909)

<br>

- ## 코드
    ```python
    def solution(s):
        stack = []
        
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if len(stack) == 0 or stack.pop() != "(":
                    return False
        
        return len(stack) == 0
    ```

    