# 12tbl_nj.py

# 오라클 tbl_nj테이블 + 파이썬
import os
import pandas as pd
import cx_Oracle  
import sys

# pip install oracledb 
import oracledb     
import time
       

config = {
    'user' : 'system',
    'password' : '1q2w3e4r!',
    'dsn' : '127.0.0.1:1521/xe'
}


# conn = oracledb.connect(**config) #오류
# conn = oracledb.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe') #오류
conn = cx_Oracle.connect(**config) 
cursor = conn.cursor()


print("database version: ", conn.version)
print("oracle connect ok success")
print()

flag = True



#신규등록전 select 이용해서
def tbl_njInsert():
    while True:
        print('\ntbl_nj테이블 신규등록 처리 ')
        dcode = int(input('코드 입력>> '))
        sql = "select count(*) from tbl_nj where code = :code"
        cursor.execute(sql, {'code': dcode})
        ret = cursor.fetchone()[0]
            
        if ret > 0:
            print("이미 존재하는 code입니다. 다른 코드를 입력하세요.")
        else :
            break

        #코드 데이터 입력 후 code 필드값 중복체크
    dname = input('이름 입력>> ')
    dtitle = input('제목 입력>> ')
    dsal = int(input('급여 입력>> '))
    msg = f"insert into tbl_nj values({dcode},'{dname}','{dtitle}',sysdate,'{dsal}', 'D')"    
    cursor.execute(msg)
    conn.commit()
    print(dcode , ' 저장 성공했습니다')
    time.sleep(1)



def tbl_njSelectAll():
    msg = 'select * from tbl_nj order by code'
    cursor.execute(msg)
    rows = cursor.fetchall()
    length = len(rows)
    if length == 0:
        return


    print('%s\t %s\t %10s\t  %8s\t %6s\t %s' %('코드','이름','제목','날짜','급여','등급') )
    for r in rows:
        # print(r[0],r[1],r[2],r[3],r[4],r[5])
        print('%4d\t %10s\t %10s\t  %8s\t %6d\t %s '%r) 
    print('전체데이터 갯수:' , len(rows))
    print('- ' * 50)
    time.sleep(1)

    #   CODE NAME  TITLE   SAL WDATE    GRADE
    #   ------ ----------- ------ ----- --------
    #   9900 goo   gugu    40 24/09/05   F
    #   8800 aaa   red     46 24/09/05   F


def tbl_njSelectTitle():
    print('제목데이터 like조회하세요 ')
    dtitle = input('제목 조회 >>>')
    msg = f"select * from tbl_nj where title like '%{dtitle}%'"
    print(msg)

def tbl_njUpdate():
    pass
    print('제목데이터 like조회하세요 ')


def tbl_njDelete():
    while True:
        tbl_njSelectAll()
        print('code 데이터 필드 값으로 삭제처리 ')
        dcode = int(input('코드 입력>> '))
        sql = "select count(*) from tbl_nj where code = :code"
        cursor.execute(sql, {'code': dcode})
        ret = cursor.fetchone()[0]
            
        if ret == 0:
            print("미등록된 code입니다. 다른 코드를 입력하세요.")
        else :
            msg = f"delete from tbl_nj where code = {dcode}"
            cursor.execute(msg)
            CN.commit()
            print('삭제 완료')
        tbl_njSelectAll()


def tbl_njExit():
    print('딕트처리를 종료합니다\n')
    sys.exit()

while flag:
    print()
    num=int(input('1등록 2출력 3수정 4삭제 5조회 9종료>>'))
    if num==9:    tbl_njExit()
    elif num==1:  tbl_njInsert()
    elif num==2:  tbl_njSelectAll()
    elif num==3:  tbl_njUpdate()
    elif num==4:  tbl_njDelete()
    elif num==5:  tbl_njSelectTitle()
    else: print('처리번호를 잘못 입력하셨습니다\n')


#tbl_njSelectAll()
tbl_njInsert()
time.sleep(0.5)
tbl_njSelectAll()
print()