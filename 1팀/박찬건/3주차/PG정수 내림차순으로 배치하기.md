# PG정수 내림차순으로 배치하기

## 문제

- 링크

[https://school.programmers.co.kr/learn/courses/30/lessons/12933](https://school.programmers.co.kr/learn/courses/30/lessons/12933)

## 풀이

sorted의 reverse 인자를 이용해 내림차순으로 변형하기

## 코드

```python
def solution(n):
    answer = ''
    s = sorted((list(str(n))), reverse=True)
    
    return int(answer.join(s))
    
```