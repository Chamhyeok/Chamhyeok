# 05os_path.py

# 리턴변수 = open(파일, 모드w/r/a, 인코딩)
# 리턴변수.close()
# 임포트문장 없어요
# ff = open(1,2,3) === with open(1,2,3) as ff:
import os.path
import sys

save_path = os.path.abspath('C:/Mtest/sample1.txt')
try:
    if not os.path.exists(save_path):
        pass # 파일 자체가 없으면 경고
        print(save_path, '대상 파일이 존재하지 않습니다.')
        #sys.exit()
    else:
        pass
except Exception as EX:
    print('에러 이유 확인:', EX)






