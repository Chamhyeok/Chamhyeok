# test

# 문제1. 변수 사용, 키보드 입력

name = input('이름: ')
age = int(input('나이: '))
gender = input('성별: ')

# 문제 2. 나이 입력 범위 20 ~ 70 사이

print('Who are you?')

print('이름: ', name)

if age < 20 :
    print('청소년은 불가능합니다.')
elif age >= 20 or age <= 30 :
    print('나이:', age,'세, 청년입니다.')
elif age >= 31 or age <= 65 :
    print('나이:', age,'세, 중년입니다.')
elif age > 66 :
    print('노년은 이용할 수 없습니다.')
else :
    pass



# 문제 3. 남자/남/Man 입력 > True || 여자/여/Woman 입력 >> False

if gender == '남자' or gender == '남' or gender == 'Man' :
    print('남자입니다')
elif gender == '여자' or gender == '여' or gender == 'Woman' :
    print('여자입니다')
else :
    print('잘못된 입력입니다. "남자/남/Man" 또는 "여자/여/Woman"을 입력하세요.')

# 문제 4. 함수화

def inputName() :
    name = input('이름: ')
    print(name)

    return name

def inputAge() :
    try:
        age = int(input('나이: '))
        if age >= 20 or age < 70 :
            print('나이: ', age, '세, 청년입니다.')
    except:
            print('20 ~ 70세만 이용가능합니다.')
        #다시 돌아가는 것?

    return age

def inputGender() :
    gender = input('성별: ')
    if gender == '남자' or gender == '남' or gender == 'Man' :
        print('남자입니다')
    elif gender == '여자' or gender == '여' or gender == 'Woman' :
        print('여자입니다')
    else :
        print('잘못된 입력입니다. "남자/남/Man" 또는 "여자/여/Woman"을 입력하세요.')

    return gender