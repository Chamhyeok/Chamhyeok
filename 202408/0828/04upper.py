# 04upper

msg = 'NewJeansHAERINKANG'

print(msg.upper())  # msg를 모두 대문자로 출력
print(msg.lower())  # msg를 모두 소문자로 출력
print('J =', msg.find('J'))    # J의 위치
print('w =', msg.index('w'))   # w의 위치

pos = msg.find('B')
if pos == -1:
    pass
    print('해당 문자열은 존재하지 않습니다.')
else:
    pass