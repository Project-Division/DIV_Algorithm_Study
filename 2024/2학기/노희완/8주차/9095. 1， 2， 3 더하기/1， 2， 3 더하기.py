# 9095 1, 2, 3 더하기

n = int(input())

for T in range(n):
    n, i = int(input()), 4
    plus = [None, 1, 2, 4]

    while i <= n:
        plus.append(plus[i - 1] + plus[i - 2] + plus[i - 3])
        i += 1

    print(plus[n])