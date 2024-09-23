# 01string

# str(), len()

x = 'HAERIN'
y = 20060515
print(x + str(y))   # y를 str형태로 변환
print(f'{x} {y}')   #분리 문자, 숫자
print(x,y)          # x,y를 따로 출력 (, >> blank)

msg = 'HAERIN20060515'
print('길이: ', len(msg))       # msg의 길이
print('갯수: ', msg.count('0')) # msg 내의 (x)의 갯수