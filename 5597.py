c = [i for i in range(1,31)]

for _ in range(28): # 28번 반복
    g = int(input()) 
    c.remove(g) # 제거

print(min(c)) #최소
print(max(c)) #최대
