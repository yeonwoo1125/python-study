import sys

li = sys.argv

print(li)

s = 0
for i in range(1, 11):
    s += int(li[i])

print(s)
