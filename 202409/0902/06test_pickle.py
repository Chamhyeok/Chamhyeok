# 06test_pickle

# open(1파일명, 2모드(wb/rb), 3인코딩)
# dump쓰기 / load읽기

import pickle
import time

fileName = 'C:/Mtest/newjeans.pckl' 
mybest = {
    '뉴진스ETA': 10.0, 
    '뉴진스Attention': 9.9, 
    '뉴진스Hypeboy': 10.1
    }

# 일반 처리 file.write('뉴진스')
pickle.dump(mybest, open(fileName, 'wb'))
print(fileName, 'pickle save complete')
print('- ' * 60)
print()

time.sleep(1)
#피클 파일 저장 dump(1,wb)/ load(1,'rb')
data = pickle.load(open(fileName, 'rb'))
print(data)