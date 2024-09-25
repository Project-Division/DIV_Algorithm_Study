# PG.자연수 뒤집어 배열로 만들기

## 문제

- 링크

[](https://school.programmers.co.kr/learn/courses/30/lessons/12932)

## 풀이

## 코드

```python
def solution(n):
    return list(map(int, list(str(n))))[-1::-1]
    
```