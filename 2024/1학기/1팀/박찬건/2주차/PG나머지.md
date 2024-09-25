# PG 나머지 1되는 수

# 문제

- 링크

[](https://school.programmers.co.kr/learn/courses/30/lessons/87389)

# 풀이

# 코드

```python
def solution(n):
    for x in range(3, n+1):
        if n % x == 1:
            return x
        
```