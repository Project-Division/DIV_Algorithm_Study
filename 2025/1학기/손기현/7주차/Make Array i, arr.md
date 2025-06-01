# 문제  
## i 보다 arr 이 더 클 때 stk 가 비면 arr 추가 i + 1, stk의 원소가 있고 그 마지막 수가 arr보다 작으면 추가 후 i + 1 크거나 같으면 마지막 원소 제거거
## [링크](https://school.programmers.co.kr/learn/courses/30/lessons/181918)
## 코드
    """ python3
    def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
            if not stk:
                stk.append(arr[i])
                i += 1
            elif stk and stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            elif stk and stk[-1] >= arr[i]:
                stk.pop()

    return stk


    """
## 요점
while문의 무한반복에 조건을 걸어서 값을 비교하여 stk에 원소를 추가하거나 뺄 수 있었다.