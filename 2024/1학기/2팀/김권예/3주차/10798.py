# 10798. ���� �б�
# 15���� ���ڸ� �޾� ���η� �д´�.
# ������ ���� �� ����ġ�� ���� ���ڸ� �д´�.

col = [input() for _ in range(5)]
maxNum = []

for i in range(5):
    n = maxNum.append(len(col[i])) # ���帶�� ������ �� ������ �޾Ƽ� ����Ʈ�� �Է�
       
for i in range(max(maxNum)): # �ִ� ���ڿ� ���̸�ŭ �ݺ�
    for j in range(5): # ���� 5���� 
        if i < len(col[j]): # i�� ���ڿ� ���� ���� ���� ������ �ݺ�
            print(col[j][i], end='')
        else:
            continue