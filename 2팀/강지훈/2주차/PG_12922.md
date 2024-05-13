# programmers / 수박수박수박수박수박수?

- ## 문제

  [링크](https://school.programmers.co.kr/learn/courses/30/lessons/12922)

- ## 코드

```Python
def solution(n):

# n이 짝수일 경우 수박을 n/2번 반복
    if n%2 == 0:
        
        a = n/2
        
        a = int(a)
        
        return '수박'*a

# n이 홀수일 경우 수박을 n/2번 반복 후에 '수'를 한번 더함
    else:
        
        b = (n-1)/2
        
        b = int(b)
        
        return '수박'*b + '수'
    
    return answer
```
