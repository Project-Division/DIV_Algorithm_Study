# 프로그래머스 _ 구명보트

- ## 문제
    - ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/42885)

<br>

- ## 코드
    ```python
    def solution(people, limit):
    answer = 0
    people.sort()  
    l, r = 0, len(people) - 1
    
    while l <= r:
        if people[l] + people[r] <= limit:  # 가장 가벼운 사람과 가장 무거운 사람의 합이 제한 이하인지 확인
            l += 1                          # 둘이 함께 탈 수 있다면 l += 1
        r -= 1                              # 항상 r -= 1(가장 무거운 사람이 보트에 탑승)
        answer += 1                        
    
    return answer
    ```