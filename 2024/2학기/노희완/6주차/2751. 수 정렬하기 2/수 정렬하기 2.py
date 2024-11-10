import sys

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    num = int(sys.stdin.readline().strip())
    lst.append(num)

lst.sort()

for i in lst:
    print(i)