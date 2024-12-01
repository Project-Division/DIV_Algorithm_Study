# 1003 피보나치 함수

n = int(input())

for i in range(n):
    num = int(input())
    a, b = 1, 0
    for j in range(num):
        a, b = b, a+b
    print(a, b)