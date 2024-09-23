# 16 def_return

def book():
    # 지역변수 = local variable (book 함수에서만 title 사용)
    title = '데이터 과학 기반의 파이썬 빅데이터 분석'   
    return title

def pay():
    price = 9500
    return price

# 일반함수 리턴값x 매개인자x
# 출력 시 None
def blue():
    color = 'blue'

def main():
    print('fn main')
    print('title', book())
    print('price', pay())
    print('color', blue())



if __name__ == '__main__':
    main()

# 함수호출
# if __name__ == '__main__':