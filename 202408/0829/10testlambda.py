# 10 testlambda

# 람다 = 익명의 함수
# 람다식 = import X
# keyword = lambda

def mysu(num) :
    cal = 3*num+5
    return cal

data = int(input('숫자 입력:'))
# print('일반식', mysu(data))
print('람다식', (lambda num:3*num+5)(data))