'''
입력으로 들어오는 모든 수의 평균 값을 계산해주는 함수(단 입력의 수는 정해지지 않았음)
'''


def avg(li):
    s = 0
    for i in li:
        s += i
    return s / len(li)


li = list()
while True:
    a = int(input('숫자 입력'))
    li.append(a)
    print(avg(li))
