# ������
# ex. 245�� ������ 245+2+4+5 = 256
# 245�� 256�� ������
# ���� ���� ������ ���ϱ�

n = int(input())
result = 0

for i in range(1,n+1):
    # str�� �ٲٰ� �� �ڸ��� ���Ͽ� m�� ����
    m = sum(map(int, str(i)))
    if i + m == n:
        # �����ڸ� �߰��Ѵٸ� i ���� �����ϰ� break
        result = i
        break
    
print(result)