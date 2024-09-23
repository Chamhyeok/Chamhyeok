# menu

import time
import sys
import datetime

menu = dict()
flag = True
num, su, sel = 0, 0, 0
msg, info, message = 'NEWJEANS', 'HAERIN', 'KANG'

dt = datetime.datetime.now()
print('처리날짜:',dt)

def menuInsert():
    key = input('메뉴 입력(KEY): >>>')
    price = input('가격 입력(VALUE): >>>')
    menu[key] = price
    print(key, '등록 완료')

def menuAllprint():
    for i,k in enumerate(menu):
        print(i+1, k, ' ', menu[k])

def menuModify():
    key = input('수정 대상 key값 입력: >>>')
    if menu.get(key) == None :
        print('입력하신 KEY값은 존재하지 않습니다.')
    else:
        menu[key] = price
        print(key, '수정 완료되었습니다.')

def menuDelete():
    key = input('삭제 대상 키 값 입력 >>>')
    if menu.get(key) == None :
        print('입력하신 KEY값은 존재하지 않습니다.')
    else:
        menu.pop(key)
        print(key, '삭제 완료되었습니다.')

def menuSearch():
    key = input('조회 대상 키 값 입력 >>>')
    if menu.get(key) == None :
        print('입력하신 KEY값은 존재하지 않습니다.')
    else:
        print(key, ':', price)

def menuQuit():
    print('QUIT')
    flag = False




while flag:
    num = int(input('1. register 2. print 3. modify 4. delete 5. check 9. quit >> '))
    if num == 9 :   menuQuit()
    elif num == 1 : menuInsert()
    elif num == 2 : menuAllprint()
    elif num == 3 : menuModify()
    elif num == 4 : menuDelete()
    elif num == 5 : menuSearch()
    else:
        print('잘못된 번호입니다.')
    
