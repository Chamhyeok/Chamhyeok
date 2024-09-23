# 16 def_return

def book():
    # 지역변수 = local variable (book 함수에서만 title 사용)
    title = '데이터 과학 기반의 파이썬 빅데이터 분석'   
    return title

def pay():
    price = 9500
    return price

def myCal(x,y,z):           #매개인자O, 리턴값O
    tot = x+y+z
    avg = tot//3
    return avg

# myCal 함수 호출 90 95 100
# myCal 함수 리턴값이 있으면 "print(함수)"
data = myCal(90,95,100)
print(data)
print(myCal(90,95,100))

# def gugudan(name, dan):     #매개인자O, 리턴값X
#     pass

# def blue():
#     color = 'blue'          #매개인자X, 리턴값X

# def main():
#     print('fn main')
#     print('title', book())
#     print('price', pay())
#     print('color', blue())



# if __name__ == '__main__':
#     main()

# 함수호출
# if __name__ == '__main__':