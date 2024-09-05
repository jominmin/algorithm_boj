X = int(input())
N = int(input())

sum = 0 #추가

for i in range(N):
    a,b = map(int,input().split()) #be careful
# c = a*b
    sum += a*b    

if X == sum:
    print('Yes')
else:
    print('No')