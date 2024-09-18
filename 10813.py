n, m = map(int,input().split())
box = [i for i in range(1,n+1)]

for _ in range(m):
    i, j = map(int,input().split())
    temp = box[i-1]
    box[i-1] = box[j-1]
    box[j-1] = temp

for b in box:
    print(b, end = " ")

'''
1. 바꿀 첫번째 박스에 담겨있던 공의 번호를 temp에 넣는다.
2. 첫번째 박스에 두번째 박스에 담겨있던 공을 넣는다.
3. 두번째 박스에 첫번째 박스에 담겨있던 공의 번호, 즉 temp의 값을 넣는다.
'''