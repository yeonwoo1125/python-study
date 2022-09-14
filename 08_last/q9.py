f = open('sample.txt','r')
scores = f.read().split('\n')

s = 0
for i in scores:
    s += int(i)

with open('result.txt','w') as f:
    f.write(str(s/len(scores)))
