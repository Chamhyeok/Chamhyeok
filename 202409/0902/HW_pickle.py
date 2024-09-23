# 06test_pickle

# open(1파일명, 2모드(wb/rb), 3인코딩)
# dump쓰기 / load읽기

import pickle
import time
import sys

path = 'C:/Mtest/myCalendar.pckl' 

while True:
    print()
    num = int(input('1. 스케줄 기록 2. 스케줄 읽기 9. 종료 >>>'))
    if num == 1:    #피클.dump()
        file = open(path, 'wb')
        memo = input("스케줄 입력:")
        pickle.dump(memo, file)
        file.close()
        print(path, '저장 성공!')
    elif num == 2:  #피클.load()
        file = open(path, 'rb')
        data = pickle.load(file)
        print(data)
        file.close()
        print(path, '읽기 성공!')
    elif num == 9:
        print('종료')
        sys.exit
        pass
    else :
        print('정확한 번호를 입력하세요.')


# mybest = {
#     '뉴진스ETA': 10.0, 
#     '뉴진스Attention': 9.9, 
#     '뉴진스Hypeboy': 10.1
#     }

# # 일반 처리 file.write('뉴진스')
# pickle.dump(mybest, open(fileName, 'wb'))
# print(fileName, 'pickle save complete')
# print('- ' * 60)
# print()

# time.sleep(1)
# #피클 파일 저장 dump(1,wb)/ load(1,'rb')
# data = pickle.load(open(fileName, 'rb'))
# print(data)