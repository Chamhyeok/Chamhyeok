# 04delpop

data = [6,5,7,8,3,5,2,4,1]
data.remove(8)  #8 삭제
data.pop()      #제일 뒤 데이터 삭제
print(data)

del data[1]     #1번째 데이터 삭제
print(data)

del data[0:2]   #0이상 2미만 위치 데이터 삭제
print(data)

data.clear()
print(data)

# remove, del, pop, clear
# remove(데이터값) // 특정 데이터 삭제
# pop(데이터 위치) // 특정 위치 데이터 삭제
# del 대상[위치]
# clear() // 전부 삭제

# append() 제일 뒤 추가
# insert(n,value) n번째 위치에 value 추가
# 추가 dict[key] = dataValue