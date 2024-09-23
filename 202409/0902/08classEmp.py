# 08classEmp.py

#파이썬에서 클래스 이름만 명시
#클래스 안에 있는 메소드 매개인자(self)
#클래스 안에 있는 메소드 호출 ob = 클래스()

class Emp:
    user_pwd = '1234'
    user_id = 'ch'
    #member변수=global variable=public variable

    def __init__(self,id,pwd) :
        self.user_id = id
        self.user_pwd = pwd
 

    def insert(self, age):
        print('전역변수 id', self.user_id)
        print('전역변수 pwd', self.user_pwd)
        print('나이:',age)
        print('insert into 처리\n')

    def delete(self):
        print('삭제처리')
        print('dict del, delete where 조건')        

ob = Emp('sky', '1123')
ob.insert(7)
ob.delete()
