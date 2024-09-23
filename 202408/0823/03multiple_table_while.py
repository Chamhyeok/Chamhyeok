# 03multiple_table_while

import time

data = input('원하는 단 입력:')
num = int(data)

x=1
while True:
    print(f'{num}*{x}={num*x}')
    x = x+1
    if x == 10 :
        break
    time.sleep(0.2)