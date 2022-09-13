'''
while문을 사용해 1~1000 까지의 수 중 3의 배수의 합 구하기
'''

i = 1
sum_3 = 0

while i <= 1000:
    if i % 3 == 0:
        sum_3 += i
    i += 1

print(sum_3)