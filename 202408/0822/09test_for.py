# 09test_for

# 변수선언없이 for 대표변수 처리

# for x in range(1, 61, 1) :
# # Q1. 5 / 1row
#     if x % 5 != 0 :
#         print(x, end='\t')
#     else :
#         print(x)

for y in range(1, 1001, 1) :
# Q2. 5 / 1row max 40
    if y % 5 != 0 :
        print(y, end='\t')
    else :
        print(y)
    if y == 40 :
        break