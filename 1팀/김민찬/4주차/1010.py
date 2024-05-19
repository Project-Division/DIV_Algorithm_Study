def combination(n, m):
    # DP 테이블 초기화: dp[i][j]는 j개의 사이트에서 i개의 사이트를 선택하는 방법의 수
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 0개를 선택하는 경우는 항상 1가지 방법이 있음 (아무것도 선택하지 않는 것)
    for i in range(m + 1):
        dp[0][i] = 1
        
    # DP 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # dp[i][j-1]: j번째 사이트를 선택하지 않는 경우
            dp[i][j] = dp[i][j - 1]
            if i <= j:
                # dp[i-1][j-1]: j번째 사이트를 선택하는 경우
                dp[i][j] += dp[i - 1][j - 1]
    
    return dp[n][m]

def main():
    # 테스트 케이스의 개수 입력
    t = int(input().strip())
    results = []
    
    for _ in range(t):
        # 각 테스트 케이스의 N과 M 입력
        n, m = map(int, input().strip().split())
        # 조합 계산 후 결과 저장
        results.append(combination(n, m))
    
    # 모든 결과 출력
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
