x, y = input().split()
H = int(x)
M = int(y)

if M < 45:
    if H == 0:
        print(23, 60-(45-M))
    else:
        print(H-1, 60-(45-M))

elif M >= 45:
    print(H, M-45)

'''
예외 처리 or 예외 없이 
'''

