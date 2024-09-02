s = int(input())
if s>= 90 and s<=100:
    print('A')
elif s>= 80 and s<=89:
    print('B')
elif s>= 70 and s<=79:
    print('C')
elif s>= 60 and s<=69:
    print('D')
else:
    print('F')

'''
'or'연산자는 두 조건 중 하나만 참이면 참
'and'연산자는 두 조건이 모두 참일때 참
'''