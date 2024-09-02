A, B = input().split()
x = int(A)
y = int(B)
print(x-y)
'''
A, B = input().split()
x = input(A)
y = input(B)
print(x-y)
1. input(A)와 input(B)의 사용: input() 함수는 문자열을 입력받는 함수입니다. 
input(A)와 input(B)는 A와 B를 문자열로 입력받는 것이 아니라, 
A와 B라는 문자열을 변수로 넘기려는 시도입니다. 
이 부분에서 문제가 발생합니다. 
실제로는 input()은 사용자로부터 입력을 받기 위한 함수이므로, 
input()의 인자로 문자열을 직접 전달하는 것이 아닙니다.

2. 입력 변환 문제: 입력된 값들은 기본적으로 문자열입니다. 
계산을 하려면 문자열을 숫자로 변환해야 합니다.
'''