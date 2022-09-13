'''
리스트 중에서 홀수에만 2을 곱하여 저장하는 코드를 리스트 내포로 표현
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
'''

numbers = [1, 2, 3, 4, 5]
result = [i * 2 for i in numbers]
print(result)
