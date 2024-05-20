# 1316. 그룹 단어 체커
# 연속된 단어로만 이루어져 있는 단어를 확인하는 것
# aabbbccb -> 그룹 단어 X
# ccazzzzbb -> 그룹 단어 O

n = int(input())
group_word = n

for i in range(n):
    word = input() # 단어 입력
    for j in range(len(word)-1): 
        if word[j] != word[j+1]: # 새로운 단어가 시작될 때
            if word[j+1] in word[:j]: # j+1번째 단어가 j번째 전까지의 단어 중에 단어가 있다면
                group_word -= 1
                break

print(group_word)