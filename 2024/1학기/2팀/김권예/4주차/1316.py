# 1316. �׷� �ܾ� üĿ
# ���ӵ� �ܾ�θ� �̷���� �ִ� �ܾ Ȯ���ϴ� ��
# aabbbccb -> �׷� �ܾ� X
# ccazzzzbb -> �׷� �ܾ� O

n = int(input())
group_word = n

for i in range(n):
    word = input() # �ܾ� �Է�
    for j in range(len(word)-1): 
        if word[j] != word[j+1]: # ���ο� �ܾ ���۵� ��
            if word[j+1] in word[:j]: # j+1��° �ܾ j��° �������� �ܾ� �߿� �ܾ �ִٸ�
                group_word -= 1
                break

print(group_word)