# 2581. �Ҽ�
# N �̻� M ������ �ڿ��� �� �Ҽ��� ã��,
# �Ҽ��� �հ� �ּҰ��� ã�Ƴ���

n = int(input())
m = int(input())
cnt = []

for i in range(n, m+1):
    if i > 1 : # �߿�! 2 �̻��� ���� �߿��� �Ҽ��� ã��
        prime = True
        for j in range(2, i):
            if i % j == 0 : # �������� 0�̶�� -> �Ҽ��� �ƴ϶��
                prime = False
                break
        if prime : # prime�� True ���
            cnt.append(i) # �Ҽ� �迭�� �߰�
        
if cnt : # cnt�� ������� �ʴٸ�
    print(sum(cnt), cnt[0], sep='\n')
else : # cnt�� ����ִٸ� -> �Ҽ��� ���ٴ� ���� ������, n,m�� 1�̶�� ���ǿ��� �۵���
    print(-1)
