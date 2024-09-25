# 프로그래머스 _ 옹알이(1)

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/120956)

<br>

- ## 코드
    ```python
    def solution(babbling):
        answer = 0
        speak = ["aya","ye","woo","ma"]    
        for i in babbling:                  
            for j in speak:                 
                if j*2 not in i:            
                    i = i.replace(j,' ')      
            if i.strip() == '':               
                answer += 1                   
        return answer
    ```

    