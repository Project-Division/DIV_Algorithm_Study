# 5073. �ﰢ���� �� ��

while True:
    t = list(map(int, input().split()))
    t.sort()
    # t1 = sorted(t)

    if t != [0, 0, 0] :
        if t[0] + t[1] > t[2] :
            if t[0] == t[1] == t[2] : # ������ ���̰� ��� ���� ��
                print("Equilateral") 
            elif t[0] == t[1] or t[1] == t[2] or t[2] == t[0] : # �� ���� ���̰� ���� ��
                print("Isosceles")
            else : # �� ���� ���̰� ��� �ٸ� ��
                print("Scalene") 
        elif t[2] >= t[1] + t[0] : # �� ���� ���̰� �ﰢ�� ������ �������� ���� ��
            print("Invalid")
        else :
            print("Error")
    else :
        break