# 프로그래머스 원하는 문자열 찾기

- ## 문제
  
    ### [링크](https://school.programmers.co.kr/learn/courses/30/lessons/181878)

    알파벳으로 이루어진 문자열 myString과 pat이 주어집니다. myString의 연속된 부분 문자열 중 pat이 존재하면 1을 그렇지 않으면 0을 return 하는 solution 함수를 완성해 주세요.

    단, 알파벳 대문자와 소문자는 구분하지 않습니다.

<br>

- ## 접근 방법

    - 두개의 주어진 문자열 myString과 pat을 비교하기 위해서 둘 다 소문자로 변환한다.
    - pat이 myString 안에 있으면 1을 리턴하고, 안에 없다면 0을 리턴한다.
 
<br>

- ## 정답

    - 코드
  
      ```python
      def solution(myString, pat):
        answer = 0
        
        if pat.lower() in myString.lower():
            answer = 1
        # else:
            # answer = 0  # 생각해보니까 위에 이미 answer=0이라고 초기화해놔서 else문은 필요없을듯
        
        return answer
      ```
