numbers = [] # 입력할 수들을 담을 리스트 만들기
for i in range(9): # 9개의 서로 다른 자연수
    i = int(input())
    number.append(i)

print(max(numbers))
print(numbers.index(max(numbers))+1)

'''
n = int(input())
l = list(map(int,input().split()))
n = list[0]
for i in range(n):
    if list[i] > n:
        list[i] = n
print(n)
print(i)
'''    
