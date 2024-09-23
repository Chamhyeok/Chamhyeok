# 04file_readlines.py

# 리턴변수 = open(파일, 모드w/r/a, 인코딩)
# 리턴변수.close()
# 임포트문장 없어요
# ff = open(1,2,3) === with open(1,2,3) as ff:
import time

file = 'C:/Mtest/sample1.txt'
with open(file,'r',encoding='UTF-8') as myfile:
    for data in myfile.readlines():
        print(data, end='')
    
time.sleep(0.5)
print(file,'파일읽기성공했습니다')
print()





