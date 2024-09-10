n, m = map(int,input().split())
basket = [0]*(n+1) #배열의 크기를 바구니의 개수만큼 만들기

for _ in range(m):
    i, j, k = map(int,input().split())
    for idx in range(i, j+1):
        basket[idx-1] = k

for i in range(n):
    print(basket[i],)

'''
1. 먼저 배열의 크기를 바구니의 개수만큼 만들고 0으로 초기화
2. i부터 j까지 배열의 값에 k를 대입한다. 
이때, 첫번째 바구니의 번호가 1번이고 
배열의 첫번째 인덱스는 0이므로 
i번째 배열의 값을 대입해주기 위해 box[idx-1] = k 로 표현
'''