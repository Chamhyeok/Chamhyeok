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
kor, eng, sum = 0, 0, 0
avg = 0.0
msg = 'Newjeans'
grade = 'F'

kor = 100
eng = 95
sum = kor + eng
avg = sum/2

if avg >= 70:
    message = '합격'
else :
    message = '불합격'

print('국어', kor)
print('영어', eng)
print('합계', sum)
print('평균', avg)
print('결과', message)