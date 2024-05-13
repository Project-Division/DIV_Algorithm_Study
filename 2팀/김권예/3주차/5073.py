# 5073. 삼각형과 세 변

while True:
    t = list(map(int, input().split()))
    t.sort()
    # t1 = sorted(t)

    if t != [0, 0, 0] :
        if t[0] + t[1] > t[2] :
            if t[0] == t[1] == t[2] : # 세변의 길이가 모두 같을 때
                print("Equilateral") 
            elif t[0] == t[1] or t[1] == t[2] or t[2] == t[0] : # 두 변의 길이가 같을 때
                print("Isosceles")
            else : # 세 변의 길이가 모두 다를 때
                print("Scalene") 
        elif t[2] >= t[1] + t[0] : # 세 변의 길이가 삼각형 조건을 만족하지 못할 때
            print("Invalid")
        else :
            print("Error")
    else :
        break