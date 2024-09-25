# PG 정수 제곱근

# 문제

- 링크

[](https://school.programmers.co.kr/learn/courses/30/lessons/12934)

# 풀이

# 코드

```python
def solution(n):
    return (n**0.5 + 1)**2 if n% (n**0.5) == 0 else -1
```