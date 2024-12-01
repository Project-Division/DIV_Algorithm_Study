# 11399 ATM

n = int(input())
p_time = list(map(int, (input().split())))

p_time.sort()

time = 0
for i in range(len(p_time)):
    for j in range(i+1):
        time += p_time[j]

print(time)