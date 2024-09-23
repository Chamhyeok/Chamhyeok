# 02list

a_list = [] # list 선언
a_dict = {} # dict 선언

a_list.append('LEE')
a_list.append(100)
a_list.append(98)
a_list.append(True)
a_list.insert(1, '수학: ') # list.insert(n, value) // n번째 자리에 value 추가
# 98 삭제하기
a_list.pop(3)


for k in a_list:
    print(k, end='\t')

# 리스트데이터 갯수 count(데이터)
cnt = a_list.count(98)
print('리스트 갯수: ', cnt)