def solution(s):
    s = s.lower()
    answer = (s.count('p') == s.count('y'))
    return answer