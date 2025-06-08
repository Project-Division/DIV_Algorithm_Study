# 문제  
## 문자열에서 l 보다 앞에 있는 단어 들을 모두 l로 바꾸어서 출력하여라라
## [링크](https://school.programmers.co.kr/learn/courses/30/lessons/181834)
## 코드
    """ python3
    def solution(myString):
    answer = ''
    for idx, val in enumerate(myString):
        if ord(val) < ord('l'):
            answer += 'l'
        else:
            answer += val
    return answer


    """
## 요점
enumerate를 이용하여 값을 유니코드로 바꾸어서 비교하여 l을 더하거나 값을 더하고 리턴하는 코드를 만들고 성공을 했는데 막상 검사하고 다시보니 이러면 굳이 enumerate를 사용할 필요가 없어보인다. 만약 enumerate를 이용한다면 myString[idx] = 'l'로 문자열을 l로 바꾼 후, 더함으로써 완성 할 수 있겠다. 게다가 python의 translate라는 함수로 myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))를 이용하여 l 앞의 영단어를 모두 바꾸어 줄 수 있다는 것도 알 수 있었다.