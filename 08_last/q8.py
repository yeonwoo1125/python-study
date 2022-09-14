f = open('abc.txt')
body = f.read().split('\n')
f.close()

body.reverse()
body = "\n".join(body)

with open('abc.txt','w') as f:
    f.write(body)
