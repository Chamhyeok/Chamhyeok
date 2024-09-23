# homework_coffee

money, sel = 0, 9

money = int(input('금액 입력: '))

while True:
    print('------------------ Coffee Machine ------------------')
    print('')
    data = int(input('1. Coffee(250) 2 Cocoa(300) 3. Return 9. Exit'))
    sel = int(data)
    if sel == 1 :
        if money < 250 :
            print('잔액이 부족합니다.')
        else :
            money = money - 250
            print('Coffee가 주문되었습니다.')
            break
    elif sel == 2 :
        if money < 300 :
            print('잔액이 부족합니다.')
        else :
            money = money - 300
            print('Cocoa가 주문되었습니다.')
            break
    elif sel == 3 :
        print('잔액', money,'원이 반환되었습니다.')
        break
    elif sel == 9 :
        print('주문을 종료합니다.')
        break
    # if~elif~if 커피값 계산

print('현재 잔액은', money, '입니다.')