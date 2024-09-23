# 07 compreehension

msg = ['spam' ,'ham','spam' ,'ham','spam' ,'spam']

for k in range(1,11):
    num = k**2
    print(num, end='\t')

for k in range(1,11):
    num = pow(k,2)
    print(num, end='\t')

# 문제 1. for반복 . if
a_list = [ a**2 for a in range(1,11)]
print(a_list)

# 문제 2. comprehension 처리