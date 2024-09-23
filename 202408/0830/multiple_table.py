# multiple_table

# 시작 진입 호출 main
# main함수 > title(), input(), output(), title()

import time

def title():
    print('* ' * 30)
    print('START!')
    print()

def num():
    data = int(input('숫자를 입력하슝 >>'))
    return data

def ret(x):
    for k in range(1,10):
        print(f'{k} * {x} = {k * x}')

def main():
    # 진입
    title()
    data = num()
    ret(data)


if __name__ == '__main__':
    main()
