# 9506. ������� ��
# �ڽ��� ������ ������� �հ� �ڽ��� ������ ��������� ��
# ������ �Ǻ� �ڵ�

while True:
    n = int(input())
    f = []
    if n == -1 : # �Է��� �������� -1
        break
    
    for i in range(1, n): 
        if n % i == 0 : # ����� ã���� ����Ʈ�� ����
            f.append(i)
            
    if sum(f) == n : # ����Ʈ(���)�� ���� n�� ���ٸ� -> ���������
        # '���̿� �߰��� ����'.join(����Ʈ)
        print(n,"=", ' + '.join(map(str, f)))
    else :
        print("%d is NOT perfect."%n)