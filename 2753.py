a = int(input())
if a % 4 == 0 and a % 100 != 0:
    print('1')

elif a % 400 == 0:
    print('1')

else:
    print('0')

'''
1. or, and 같이 쓰기
year = int(input())

if ((year%4 == 0)and(year%100 != 0)) or (year%400 == 0):
    print('1')
else:
    print('0')

2. 삼항 연산자
year = int(input())

print('1') if ((year%4 == 0)and(year%100 != 0)) or (year%400 == 0) else print('0')
'''

