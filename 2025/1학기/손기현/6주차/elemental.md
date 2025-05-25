# 문제 
## 리스트의 마지막과 그 전의 원소를 비교하여 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 리턴하여라라
## [링크](https://school.programmers.co.kr/learn/courses/30/lessons/181927)
## 코드
    """ python3
    def solution(num_list):
        if num_list[-1] > num_list[-2]:
            num_list.append(num_list[-1] - num_list[-2])
        else:
            num_list.append(num_list[-1] * 2)
    
        return num_list

    """
## 요점
리스트의 순서는 0,1,2,3,...이지만 ..., -3,-2,-1,0,1,2로 음수는 마지막을 가리킨다.