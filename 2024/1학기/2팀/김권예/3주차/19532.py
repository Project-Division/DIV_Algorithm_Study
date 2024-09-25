# 19532. 수학은 비대면강의입니다
# 브루트포스
# 발생 가능한 모든 경우의 수 대입해서 해를 구하는 방식
# 연립 방정식을 구하는 문제

func = list(map(int, input().split()))

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (func[0]*i) + (func[1]*j) == func[2] and (func[3]*i) + (func[4]*j) == func[5]:
            print(i,j)