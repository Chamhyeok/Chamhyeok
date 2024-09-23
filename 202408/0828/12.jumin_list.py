# 09 jumin

import datetime
import time

jumin = '950327-1649753'

# 12시 15분 split() 사용


# 문제 3. 나이계산 2024 - 1995

a_list = list(jumin.split('-'))

b_info = a_list[0][2:]
g_info = a_list[1][0]
year = a_list[0][0:2]

last = a_list[1][:]
print('주민번호 뒷자리:', last)
today = datetime.datetime.now()
print(today)

# 문제 1. 성별 check
if g_info == '1' or g_info == '3':
    print('남성입니다.')
elif g_info == '2' or g_info == '4':
    print('여성입니다.')
else:
    print('성별 표기 오류입니다.')

if (jumin.split('-')[1][0] == '1') or (jumin.split('-')[1][0] == '3'):
    print('남성입니다.')
elif (jumin.split('-')[1][0] == '2') or (jumin.split('-')[1][0] == '4'):
    print('여성입니다.')
else:
    print('성별 표기 오류입니다.')

# 문제 2. 생일 3월 27일 HBD!!


# if datetime.datetime.now() == 