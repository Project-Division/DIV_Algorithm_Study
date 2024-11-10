import sys

n = int(sys.stdin.readline())
word = []

for i in range(n):
    word.append(sys.stdin.readline().strip())

set_word = set(word) # 리스트를 집합으로 변환, 중복 제거
word = list(set_word) # 집합을 리스트로 변환

word.sort()	# 괄호 안에 아무 값도 넣지 않으면 알파벳 순서대로 정렬을 해 준다.
word.sort(key = len) # 문자열 길이 순으로 정렬.

for i in word:
    print(i)