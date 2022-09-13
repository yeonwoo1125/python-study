'''
주어진 자연수가 홀수인지 짝수인지 판별해주는 함수(is_odd) 작성
'''


def is_odd(a):
    return a % 2 == 0


if is_odd(13):
    print('짝수')
else:
    print('홀수')
