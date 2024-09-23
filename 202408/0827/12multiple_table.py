# 11multiple_table

# 파이썬 함수 def 함수이름 ()
# 파이썬 함수 매개인자
# 파이썬 함수 리턴값    
# 함수는 호출call

# 내장함수
# ex) list(), len(), tuple(), set(), str(), int(), round(), print(), input()


def mutiple_table(name, n):
    print('세젤귀:', name)
    for k in range(1,10):
        print(f'{n} * {k} = {n*k}')

data = 0
try:
    data = int(input('몇 단??'))
except:
    print('정수 숫자를 입력해!!')

mutiple_table('찬돌', data)

