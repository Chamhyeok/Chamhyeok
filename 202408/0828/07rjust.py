# 07 rjust

for x in range(1,6):
    pass
    # print(f'{x} * {x} = {x*x}')
    print(x, '*', x, '=', (x*x))
print()
for x in range(1,6):
    print(x, '*', x, '=', str(x*x).rjust(5))    # 연산 결과 str 변환 후 우정렬

for x in range(1,6):
    print(x, '*', x, '=', str(x*x).zfill(6))    # 연산 결과 str 변환 후 우정렬