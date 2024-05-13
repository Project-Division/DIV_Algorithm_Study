# programmers / 약수의 합

- ## 문제

  [링크](https://school.programmers.co.kr/learn/courses/30/lessons/12928)

- ## 코드

```Python
def solution(n):
    s = 0
    for i in range(1, n+1):
        if n%i==0:
            s+=i
    return s
```
