# 10815. ���� �迭
# ���հ� ��

N = int(input())
NN = set(map(int, input().split()))

M = int(input())
MM = list(map(int, input().split()))

for i in MM: 
    r = 0 # �ʱ� ����� r�� 0���� ����
    if i in NN: # ���� ���� ���� i�� ���� NN�� ������
        r = 1 # ����� r�� 1�� ����
    print(r, end=" ")
 