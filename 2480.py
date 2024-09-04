x, y, z = input().split()
A = int(x)
B = int(y)
C = int(z)

if A == B == C:
    print(10000+A*1000)

elif A==B:
    print(1000 + A*100)
      
elif B == C:
    print(1000 + B*100)

elif A == C:    
    print(1000 + A*100)

else:
    print(100*max(A,B,C)) # 여러 개 중 가장 많은 것

'''
위에 있는 조건에 포함되는 조건은 추가하지 말기
나머지 else도 때에 따라 잘 쓰기
if A == B == C:
    print(10000+A*1000)

elif A==B and B != C:
    print(1000 + A*100)
      
elif B == C and C != A:
    print(1000 + B*100)

elif A == C and B != C:    
    print(1000 + A*100)

elif A != B != C:
    print()
'''