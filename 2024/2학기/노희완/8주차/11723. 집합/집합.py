import sys
input = sys.stdin.readline

n = int(input())
s = set()

for _ in range(n):
    cmd = input().strip().split()
    
    if len(cmd) == 1:  # all 또는 empty 명령어
        if cmd[0] == "all":
            s = set(range(1, 21))
        else:  # empty
            s = set()
        continue
        
    op, x = cmd[0], int(cmd[1])  # 명령어와 숫자를 분리
    
    if op == "add":
        s.add(x)
    elif op == "remove":
        s.discard(x)
    elif op == "check":
        print(1 if x in s else 0)
    elif op == "toggle":
        if x in s:
            s.discard(x)
        else:
            s.add(x)