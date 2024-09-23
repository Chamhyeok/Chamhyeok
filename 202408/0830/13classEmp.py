# 13classEmp.py

#파이썬에서 클래스 이름만 명시
#클래스 안에 있는 메소드 매개인자(self)
#클래스 안에 있는 메소드 호출 ob = 클래스()

class Emp:
    def insert(self):
        print('신규등록')
        print('dict 등록, 파일 저장, insert into 처리')
        print('insert into 처리\n')

    def delete(self):
        print('삭제처리')
        print('dict del, delete where 조건')        

ob = Emp()
ob.insert()
ob.delete()

print
print('9월 2일 월요일')