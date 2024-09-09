n = int(input())
l = list(map(int,input().split()))
max = l[0] # 가장 처음으로 정하기
min = l[0]

for i in l[1:]: # 그냥 반복문을 list 안에서
    if i > max:
        max = i
    elif i < min:
        min = i
# list 처음부터 max,min과 비교하며 값 도출
print(min,max)