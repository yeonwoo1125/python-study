import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    with open('memo.txt','a') as f:
        f.write(memo)
        f.write('\n')

elif option == '-v':
    with open('memo.txt') as f:
        data = f.read()
        print(data)
else:
    print('메모 입력 : -a, 메모 읽기 : -v')
