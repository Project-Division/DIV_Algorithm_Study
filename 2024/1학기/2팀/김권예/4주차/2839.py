# 2839. ���� ��� (���Ʈ ����)

n = int(input())
cnt = 0 # ��� ����

# �ּ� ���
if n % 5 == 0 : # 5kg�� ���� ������ ��
    print(n // 5)
else : # 3kg, 5kg �� ������ ����ؾ��� ��
    while True:
        if n % 5 != 0: # 5�� �������� ���� ��
            n = n - 3 # + 3kg
            cnt += 1
        elif n % 5 == 0:
            cnt += n // 5
            print(cnt)
            break
        if n < 0:
            print(-1)
            break