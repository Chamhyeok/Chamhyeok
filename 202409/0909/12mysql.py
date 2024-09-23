#12mysql

import pymysql
config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '1234',
    'database' : 'naver',
    'port' : 3306
}
CN = pymysql.connect(**config)
cursor = CN.cursor()

msg = "select * from test"

def dbInsert():
    pass

dbInsert()
print()


msg = "select * from test "
cursor.execute(msg)
rows = cursor.fetchall()
for r in rows:
    print(r[0], r[1], r[2], r[3] )
print('레코드갯수 ', len(rows))