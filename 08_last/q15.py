n = input()
n = list(n)


def dup(num):
    res = list()
    for i in num:
        if i not in res:
            res += i
        else:
            return False
    return len(res) == 10


print(dup(n))
