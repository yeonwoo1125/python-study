'''
"test.txt.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력
'''

f1 = open('test.txt.txt','a')
f1.write('Life is too short')

f2 = open('test.txt.txt','r')
print(f2.readline())