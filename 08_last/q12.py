result = 0

try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
    print(1)
except ZeroDivisionError:
    result += 2
    print(2)
except IndexError:
    result += 3
    print(3)
finally:
    result += 4

print(result)