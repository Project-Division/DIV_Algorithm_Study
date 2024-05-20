# PG 내적

## 문제

- 링크

[https://school.programmers.co.kr/learn/courses/30/lessons/70128](https://school.programmers.co.kr/learn/courses/30/lessons/70128)

## 풀이

## 코드

```python
def solution(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])
```