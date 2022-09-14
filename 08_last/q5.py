num = int(input('숫자 입력 : '))


def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fibo(num))
