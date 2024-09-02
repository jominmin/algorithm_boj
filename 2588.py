A= int(input())
B= input()
print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))

'''
정수형은 인덱싱(B[2])할 수 없음
'''

A = int(input())
B = input()

for i in range(3, 0 ,-1):
    print(A*int(B[i-1]))
print(A*int(B))

'''
range(start, stop, step)
start: 범위의 시작 값 (기본값: 0)
stop: 범위의 끝 값
step: 증가 값(기본값:1) range()함수를 호출하면 start부터 stop-1까지 step만큼 증가하는 정수의 시퀀스를 반환합니다.
'''