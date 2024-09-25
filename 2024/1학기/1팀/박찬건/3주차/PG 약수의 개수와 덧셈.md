# PG 약수의 개수와 덧셈

## 문제

- 링크

[https://school.programmers.co.kr/learn/courses/30/lessons/77884](https://school.programmers.co.kr/learn/courses/30/lessons/77884)

## 풀이

## 코드

```python
def divisor(n):
    a = 0
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            a += 1
            if i != n//i:
                a += 1
    return a

def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        if divisor(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
```