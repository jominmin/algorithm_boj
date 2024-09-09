a, b = map(int,input().split())
c = list(map(int,input().split()))

for i in range(a):
    if c[i] < b:
        print(c[i], end = " ")

# 반복문으로 list를 하나하나 찾기