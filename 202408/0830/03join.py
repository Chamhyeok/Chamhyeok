# 03 join

url = 'www.google.com'
print(url)

result = url.split('.')     #.을 기준으로 구분(자동으로 리스트화)

conn = ';'
print(conn.join(url))