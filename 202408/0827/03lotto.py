# 03lotto

lotto = [ 3, 16, 22, 16, 11, 3, 41, 33 ]
a_set = set(lotto)
print(a_set)
lotto = list(a_set) #오름차순 적용을 위해 list로 변경
lotto.sort()        #오름차순 적용
a_len = len(lotto)
if a_len < 6 :
    print('항목 ',6-a_len,'개 추가가 필요합니다.')
elif a_len > 6 :
    print('항목 ',a_len-6,'개 제거가 필요합니다.')
elif a_len == 6 :
    print(a_len)
    
# lotto.sort()
# print(lotto)

# 조건 1: 숫자 6개
# 조건 2: 중복 숫자 제거
# 조건 3: 정수 숫자로만 구성