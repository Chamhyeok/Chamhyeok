# 02 def_list

def a_sum(*args):
    print('*args타입', type(args))
    sum = 0
    for num in args:
        sum = sum + num
    return sum

# data = a_sum(7,8,1,4,3,3)
# print('데이터 결과:', data)
# print('데이터 결과:', a_sum(7,8,1,4,3,3))

mylist = [6,11,24,7]    # 수정 가능
mytuple = (6,11,24,7)   # 수정 불가
