# 값 할당
A, B, C = map(int, input().split())

# (A+B)%C를 계산
print((A + B) % C)

# ((A%C) + (B%C))%C를 계산
print(((A % C) + (B % C)) % C)

# (A×B)%C를 계산
print((A * B) % C)

# ((A%C) × (B%C))%C를 계산
print(((A % C) * (B % C)) % C)
