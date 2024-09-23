# 01 def_list

def data_sum(x,y,z,a,b,c):
    # 숫자 합 구해서 리턴
    sum = x+y+z+a+b+c
    return sum

def a_sum(*args):
    print('*args타입', type(args))
    sum = 0
    for num in args:
        sum = sum + num
    return sum

data = a_sum(7,8,1,4,3,3)
print('데이터 결과:', data)
print('데이터 결과:', a_sum(7,8,1,4,3,3))

print()

tot = data_sum(7,8,1,4,3,1)
print('합계:', tot)
print('합계:', data_sum(7,8,1,4,3,1))