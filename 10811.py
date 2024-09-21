N, M = map(int,input().split())
basket = [i for i in range(1,N+1)]
for i in range(M): # ()안의 범위 명확하게 설정
    i, j = map(int,input().split())
    temp = basket[i-1:j] # 새로운 리스트 생성(i부터 j까지)
    temp.reverse() # 역으로 생성
    basket[i-1:j] = temp
for i in range(N):
    print(basket[i], end = ' ')

    # for k in range(i,j): #3,6



