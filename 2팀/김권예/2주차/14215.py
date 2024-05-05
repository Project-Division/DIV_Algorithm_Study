# 가장 큰 둘레의 삼각형 구하기
# 첫 번째, 두 번째로 작은 변의 길이와 두 변의 합에서 -1 한 것이 가장 긴 변의 길이 

rect = list(map(int,input().split()))
rect.sort()
max_edge = rect[0] + rect[1] -1

# 삼각형을 이룰 수 있는 가장 큰 값(max_edge)이 rect[2]보다 작다면,
# rect[2]를 가장 긴 변으로 하여 삼각형 둘레 구함
if rect[2] < max_edge : 
    print(rect[0]+rect[1]+rect[2])    
else : 
    print(rect[0]+rect[1]+max_edge)    
