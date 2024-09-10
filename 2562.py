numbers = [] # 입력할 수들을 담을 리스트 만들기
for i in range(9): # 숫자를 입력하고 그 숫자를 앞서 만든 numbers 리스트에 담는 것을 9번 반복
    i = int(input())
    numbers.append(i)

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
