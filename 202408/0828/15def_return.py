# 15 def_return

def book():
    # 지역변수 = local variable (book 함수에서만 title 사용)
    title = '데이터 과학 기반의 파이썬 빅데이터 분석'   
    return title

def pay():
    price = 9500
    return price

def main():
    print('fn main')
    print('title', book())
    print('price', pay())
    # data = book()
    # value = pay()
    # print('title', data)
    # print('price', value)



if __name__ == '__main__':
    main()

# 함수호출
# if __name__ == '__main__':