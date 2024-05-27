# 25305. 커트라인
# 정렬

n, k = map(int, input().split()) # 응시자 수, 사람 수
x = list(map(int, input().split()))
x.sort() # 정렬
x.reverse() # 리스트 뒤집기

print(x[k-1]) # 2등까지 수여
    
