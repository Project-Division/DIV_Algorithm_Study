# 문제  
## idx 보다 큰 배열에서 값이 1인 가장 작은 arr의 인덱스를 리턴하고 아니면 -1 을 리턴하여라
## [링크](https://school.programmers.co.kr/learn/courses/30/lessons/181898)
## 코드
    """ python3
    def solution(arr, idx):
    answer = 0
    for i in range(len(arr)):
        if i >= idx and arr[i] == 1:
            answer = i
            return answer
    return -1


    """
## 요점
arr의 개수만큼 반복하는 반복문에서 idx 보다 크고 arr의 값이 1이라면 그 값을 리턴하고 아니라면  -1을 리턴하였다. 그리고 try를 사용하여 arr.index(1,idx)로 값이 1이고 idx 부터 시작하여 찾도록 반복하고 except로 없을 경우 -1을 리턴시키도록 할 수 있다.