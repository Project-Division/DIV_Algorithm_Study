# 25305. ĿƮ����
# ����

n, k = map(int, input().split()) # ������ ��, ��� ��
x = list(map(int, input().split()))
x.sort() # ����
x.reverse() # ����Ʈ ������

print(x[k-1]) # 2����� ����
    
