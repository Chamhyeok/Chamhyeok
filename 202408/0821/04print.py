# a = 7 
# b = 4
# result = 0
# message = '안내문'

a, b, result = 7, 4, 0
result = a*b
msg = 950327

# print( ' {} * {} = {}'.format(a,b,result) ) // format 사용
print('{} * {} = {}'.format(a,b,result),'format 사용')
print('{}'.format(msg))
print('{:0>10}'.format(msg))    #0000950327
print('{:*>10}'.format(msg))    #****950327
print('{:,}'.format(msg))       #950,327

'''
print(result)
print(a, '*', b, '=', result)

# print('%d * %d = %d' %(a,b,result)) '%d:정수, %s:문자열, %f:실수, %c:문자'
print('%d * %d = %d' %(a,b,result),'% 사용')

# print( f'{변수}') // format 적용
print(f'{a} * {b} = {result}','변수 직접 삽입')
'''