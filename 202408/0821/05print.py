# define var
msg = 950327

# print( ' {} * {} = {}'.format(a,b,result) ) // format 사용
print('{}'.format(msg))
print('{:>10}'.format(msg))    #||||950327 (10자리 우정렬)
print('{:<10}'.format(msg))    #950327|||| (10자리 좌정렬)
print('{:^10}'.format(msg))    #||950327|| (10자리 중앙정렬)
print()
print('-'*100)
print('{:0>10}'.format(msg))    #0000950327
print('{:*>10}'.format(msg))    #****950327
print('{:,}'.format(msg))       #950,327
