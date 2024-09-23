# 07test_for

# 문자열 출력, list, tuple, set, dict
# 반복데이터

'''
for x in range(5) :
    5회처리 (0~4)

for x in range(1,5) :
    4회처리 (1~4)

for x in range(1,5,1) :
    4회처리 (1~4)
    1씩 증가할 때 3번째 1생략

while 조건 :
    조건 만족 시 loop
    무한루프 시 if문으로 break 반복 탈출
'''

a,b = 0,0
sum,tot = 0,0

# a = a+1; sum = sum + a; print(a, sum)
# a = a+1; sum = sum + a; print(a, sum)
# a = a+1; sum = sum + a; print(a, sum)

for a in range(5) :
    a = a + 1
    sum = sum + a
    print(a, sum)
    