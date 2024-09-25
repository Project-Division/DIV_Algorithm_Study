# 1018. 체스판 다시 칠하기
# 브루트 포스

n, m = map(int, input().split())
arr = []
res = []

for i in range(n):    
	arr.append(list(map(str, input())))

for x_start in range(0, n-7): # 8x8 체스판을 구할 수 있는 모든 경우의 수를 반복
    for y_start in range(0, m-7):
        cntB = 0
        cntW = 0
        for x in range(x_start, x_start+8):
            for y in range(y_start, y_start+8):
                if (x+y) % 2 == 0  :
                    # (0,0) -> W 일 때
                    if arr[x][y] != 'B' :
                        cntB += 1
                    # (0,0) -> B 일 때
                    if arr[x][y] != 'W':
                        cntW += 1
                else :
                    # (0,0) -> W 일 때
                    if arr[x][y] != 'W' :
                        cntB += 1
                    # (0,0) -> B 일 때
                    if arr[x][y] != 'B':
                        cntW += 1
        res.append(cntB)
        res.append(cntW)
print(min(res))
    
    
             
