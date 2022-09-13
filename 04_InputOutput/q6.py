'''
사용자가 입력한 내용을 test1.txt 파일에 저장
'''

a = input('내용 입력 : ')
with open('test1.txt', 'a') as f:
    f.write(a)

with open('test1.txt','r') as f:
    print(f.readline())