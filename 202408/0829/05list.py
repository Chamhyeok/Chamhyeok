# 05 list

lotto = [13, 28, 39, 1, 25, 22]

for k in range(1,11):
    num = k**2
    print(num, end='\t')

for k in range(1,11):
    num = pow(k,2)
    print(num, end='\t')

a_list = [ a**2 for a in range(1,11)]
print(a_list)

a_tuple = ( pow(b,2) for b in range(1,11))
print(a_tuple)

a_set = { c**2 for c in range(1,11)}
print(a_set)