# 프로그래머스 - 불량 사용자

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/64064)

<br>

- ## 설계
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/dce51d06-5bfb-491a-b973-bf4a0082f310)

<br>

- ## 코드
    ```python
    def pattern_match(word, pattern):
        if len(word) != len(pattern): return False
        for i in range(len(pattern)):
            if pattern[i] == "*":
                continue
            if pattern[i] != word[i]:
                return False
        return True

    visited = set()
    result = 0
    def make_case(items, selected, depth):
        global result
        
        if depth == len(items):
            if tuple(sorted(selected)) in visited:
                return
            visited.add(tuple(sorted(selected)))
            # print(selected)
            result += 1
            return
        
        for item in items[depth]:
            if item in selected:
                continue
            selected.append(item)
            make_case(items, selected, depth + 1)
            selected.pop()

    def solution(user_id, banned_id):
        global result
        
        match = []
        for i_bid, bid in enumerate(banned_id):
            curr_match = set()
            for uid in user_id:
                if pattern_match(uid, bid):
                    if uid in curr_match:
                        continue
                    curr_match.add(uid)
            match.append(curr_match)
            
        make_case(match, [], 0)
        
        return result
    ```

<br>

- ## 결과
    ![image](https://github.com/Project-Division/DIV_Algorithm_Study/assets/68108664/1ef13aaa-e4ef-4a3d-9568-f2d0ba0f7948)