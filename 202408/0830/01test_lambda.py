# 01test_lambda

def myCheck(num):
    nmg = num // 2
    if nmg == 0 :
        print('짝수입니다.')
    elif nmg == 1 :
        print('홀수입니다.')
    else:
        print('정수가 아닙니다.')

print((lambda num: '짝수' if num % 2 == 0 else '홀수')(12))