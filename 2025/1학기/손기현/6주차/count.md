# 문제 
## 시작 값과 끝 값을 받았을 때 처음 값부터 끝 값까지 모두 더한 리스트를 출력하여라라
## [링크](https://school.programmers.co.kr/learn/courses/30/lessons/181920)
## 코드
    """ python3
    def solution(start_num, end_num):
        answer = []
        for i in range(end_num - start_num + 1):
            answer.append(start_num)
            start_num += 1
        return answer

    """
## 요점
return 에 list(range(start,end+1))로 한번에 리스트화 할 수 있다..