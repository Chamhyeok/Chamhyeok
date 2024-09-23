# 08test_for

# 변수선언없이 for 대표변수 처리

for x in range(1, 31, 1) :
    #print(x)            # print() 자동 \n
    #print(x, end='\t')  # \t: tab
    if x % 5 != 0 :
        print(x, end='\t')
    else :
        print(x)
