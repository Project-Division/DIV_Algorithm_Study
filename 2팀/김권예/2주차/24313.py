# 시간 복잡도 - 점근적 표기
# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
# f(n) = an + b
# g(n) = n

a, b = map(int, input().split())
c = int(input())
n = int(input())

# b가 음수일 때, a <= c 가 성립해야 함
if (a*n + b) <= (c*n) and a-c <= 0 : 
    print(1)
else :
    print(0)
