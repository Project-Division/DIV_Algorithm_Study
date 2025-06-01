# 문제  
## 인덱스 배열 값으로 my_string의 인덱스의 값을 answer에 넣어 리턴하여라라
## [링크](https://school.programmers.co.kr/learn/courses/30/lessons/181915)
## 코드
    """ python3
    def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer



    """
## 요점
for i in index_list로 배열 크기만큼 반복하여 차례차례로 answer에 더한 후, 리턴할 수 있었다.