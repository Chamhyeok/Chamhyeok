# for if

'''
if condition1 :
    stn1 satisfied
elif condition2 :
    stn2 satisfied
elif condition3 :
    stn3 satisfied        
else :
    unsatisfied
'''
# declare
a, b, c = 7, 2, 4
z, y, z = False, False, False

# 관계연산 (비교연산)  > < >= <= == !=
# 논리연산 and or not is in
x = ( (a >= b) and ( b >= c) )
y = ( (a >= b) or  ( b >= c) )
z = ( a != b )

print('논리연산 and or test')
print(x)
print(y)
print(z)
