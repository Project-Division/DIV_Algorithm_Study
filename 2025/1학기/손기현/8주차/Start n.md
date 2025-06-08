# 문제  
## n부터 리스트의 끝까지 원소를 받은 리스트를 리턴하여라라
## [링크](https://school.programmers.co.kr/learn/courses/30/lessons/181892)
## 코드
    """ python3
    def solution(num_list, n):
    answer = []
    for i in range(n-1,len(num_list)):
        answer.append(num_list[i])
    return answer


    """
## 요점
n은 인덱스를 의미하므로 n-1 부터 시작하여 num_list의 개수 만큼 반복하여 answer 리스트에 추가하여 값을 리턴하도록 할 수 있었는데 슬라이싱을 이용한다면 num_list[n-1:]로 리스트를 받아 리턴할 수 있다.