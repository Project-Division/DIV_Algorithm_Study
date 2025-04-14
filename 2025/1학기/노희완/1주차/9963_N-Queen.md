# [Gold IV] N-Queen - 9663 

[문제 링크](https://www.acmicpc.net/problem/9663) 

![N-Queen](https://github.com/user-attachments/assets/580cc505-e011-4574-9f8b-af3efaa2a99b)

### 🗝️알고리즘 분류
- 백트래킹

---

<br>

## 💻문제 정의

NxN 크기의 체스판에 N개의 퀸이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 문제이다.

<br>

## 💡접근 및 설계

퀸은 상하좌우대각선 8방향으로 움직일 수 있다. 즉, 같은 열, 같은 행, 같은 대각선 내 두 개 이상의 퀸이 존재하지 않도록 퀸을 배치해야 한다.

NxN의 공간에서 N개의 퀸을 놓기 위해 백트래킹을 활용한다. 먼저 퀸을 한 개 놓고 난 다음, 두 번째 퀸을 어디에 놓을 수 있을지를 판단한다. N개의 퀸을 놓았다면 카운트를 증가하고 N-1로 돌아가 다음 경우의 수를 생각한다. 해당 과정이 백트래킹이다.

<br>

### ✏️알고리즘 풀이

```python
count = 0
row = [0 for _ in range(N)] # 한 행에는 하나의 퀸만 존재 가능

def check(x):
    for i in range(x):
        if (row[i] == row[x]) or (abs(row[x] - row[i]) == abs(x - i)): # 같은 열인지, 대각선에 겹치는지 체크
            return False
        
    return True
```

퀸이 어느 한 위치에 놓였을 때, 상하좌우대각선에 퀸이 존재하는지를 체크하는 함수이다.

row 리스트를 1차원으로 놓은 이유는, 퀸이 놓인 행에는 더 이상 다른 퀸이 존재할 수 없기 때문이다. 즉, row[1] = 2 라고 가정하면, (1, 2)의 위치에 퀸이 놓였다고 생각할 수 있다. row[1]의 값은 2로 고정일 수 밖에 없다.

다음은 대각선 위치를 판별하는 방법이다.

row[1] =2, 즉 (1, 2)의 위치에 있을 경우, 오른쪽 대각선인 (2, 3), (3, 4) ... 와 왼쪽 대각선 (2, 1), (3, 0) ... 을 확인해야 한다.

(a, b)일 때, a 끼리의 차와 b 끼리의 차의 절댓값이 같을 경우, 대각선 좌표임을 확인할 수 있다.

따라서 위의 경우에 해당할 경우 False를 반환, 그 외 경우 True를 반환한다.

<br>

``` python
def nQueen(k):
    global count

    if (k == N):
        count += 1
        return
    
    else:
        for i in range(N):
            # [k, i]에 퀸을 놓음
            row[k] = i
            if check(k):
                nQueen(k+1)

nQueen(0)
```

K는 퀸의 개수라 생각하면 편하다.

먼저 (0, i)에 퀸을 놓는다. check(0)은 True를 반환한다.

이후 (1, i)에 새로운 퀸을 놓는다. 이때 check(1)를 하는 과정에서, row[0]과 row[1]이 같다면 False를 반환한다. 

(1, i)에 놓인 퀸은 없애고 (1, i+1)에 퀸을 놓는다. 


다음의 과정을 반복하다 k == N이 되면, count를 증가시켜 경우의 수 하나를 더한다.

<br>

### 🗒️전체 코드
``` python
# 9663 N-Queen

N = int(input())

count = 0
row = [0 for _ in range(N)] # 한 행에는 하나의 퀸만 존재 가능

def check(x):
    for i in range(x):
        if (row[i] == row[x]) or (abs(row[x] - row[i]) == abs(x - i)): # 같은 열인지, 대각선에 겹치는지 체크
            return False
        
    return True

def nQueen(k):
    global count

    if (k == N):
        count += 1
        return
    
    else:
        for i in range(N):
            # [k, i]에 퀸을 놓음
            row[k] = i
            if check(k):
                nQueen(k+1)

nQueen(0)
print(count)
```

---

### [[Python] 9663 - N-Queen](https://do-heewan.tistory.com/148)