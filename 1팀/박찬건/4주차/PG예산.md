# PG 예산

## 문제

- 링크

[https://school.programmers.co.kr/learn/courses/30/lessons/12982](https://school.programmers.co.kr/learn/courses/30/lessons/12982)

## 풀이

## 코드

```python

def solution(d, budget):
    answer = 0
    d.sort()

    for i in d:
        budget -= i
        if budget < 0:
            return answer
        answer += 1

    return answer
```