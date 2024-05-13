# PG 음양더하기

## 문제

- 링크

[https://school.programmers.co.kr/learn/courses/30/lessons/76501](https://school.programmers.co.kr/learn/courses/30/lessons/76501)

## 풀이

## 코드

```python
def solution(absolutes, signs):
    ans = 0
    for i, value in enumerate(absolutes):
        if signs[i]:
            ans += value
        else:
            ans -= value
    return ans
```