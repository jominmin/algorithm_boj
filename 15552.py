import sys #추가

n = int(input())
for i in range(n):
    a, b = map(int,sys.stdin.readline().split()) 
    print(a+b)

'''
input() 아니고 sys.stdin.readline()
sys.stdin.readline() - 속도가 빠르다
- 개행문자 입력받음 
'''