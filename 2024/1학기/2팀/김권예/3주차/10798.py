# 10798. 세로 읽기
# 15개의 글자를 받아 세로로 읽는다.
# 공백이 있을 시 지나치고 다음 글자를 읽는다.

col = [input() for _ in range(5)]
maxNum = []

for i in range(5):
    n = maxNum.append(len(col[i])) # 문장마다 글자의 총 개수를 받아서 리스트에 입력
       
for i in range(max(maxNum)): # 최대 문자열 길이만큼 반복
    for j in range(5): # 세로 5글자 
        if i < len(col[j]): # i가 문자열 길이 보다 작을 때까지 반복
            print(col[j][i], end='')
        else:
            continue