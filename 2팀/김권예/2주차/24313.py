# �ð� ���⵵ - ������ ǥ��
# O(g(n)) = {f(n) | ��� n �� n0�� ���Ͽ� f(n) �� c �� g(n)�� ���� ��� c�� n0�� �����Ѵ�}
# f(n) = an + b
# g(n) = n

a, b = map(int, input().split())
c = int(input())
n = int(input())

# b�� ������ ��, a <= c �� �����ؾ� ��
if (a*n + b) <= (c*n) and a-c <= 0 : 
    print(1)
else :
    print(0)
