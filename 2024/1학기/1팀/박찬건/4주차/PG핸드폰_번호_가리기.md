# PG 핸드폰 번호 가리기

## 문제

- 링크

[https://school.programmers.co.kr/learn/courses/30/lessons/12948](https://school.programmers.co.kr/learn/courses/30/lessons/12948)

## 풀이

## 코드

```python
def solution(phone_number):
    return '*'*(len(phone_number)-4) + phone_number[-4::1]
```