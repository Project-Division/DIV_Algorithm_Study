# 19532. ������ ���鰭���Դϴ�
# ���Ʈ����
# �߻� ������ ��� ����� �� �����ؼ� �ظ� ���ϴ� ���
# ���� �������� ���ϴ� ����

func = list(map(int, input().split()))

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (func[0]*i) + (func[1]*j) == func[2] and (func[3]*i) + (func[4]*j) == func[5]:
            print(i,j)