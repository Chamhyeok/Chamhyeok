# 17list_for

# list [] // 반복O, 작성 순서대로 나열
a_list= ['Newjeans', 3]
print(a_list)

a_list.append('HAERIN')
print('a', a_list)

a_list.append('HANNI')
print('b', a_list)

# insert (원하는 위치, 원하는 데이터)
a_list.insert(1, 'MINJI')
print('c', a_list)
print('- ' * 50)

# list[x] = data // 원하는 위치의 값을 data로 변경
a_list[2] = 'DANIEL'
print(a_list)


# remove(data) // 원하는 data를 삭제
# a_list.remove('MINJI')

# pop(x) // x번째 data 삭제
# a_list.pop(1)

# del a_list[x] // x번째 data 삭제

# *sort() // 같은 타입의 데이터만 가능
a_list.sort()


# for 반복문 연습

# for x in range(1,11) :
#     print(x, end=' ')