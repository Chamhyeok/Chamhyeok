# homeworkmilk.py

apart = [
    [101, 102, 103, 104],
    [201, 202, 203, 204],
    [301, 302, 303, 304],
    [401, 402, 403, 404]
]

unpaid = [103, 204, 301, 402]


for a in apart:
    for b in a:
        if b in unpaid:
            print(f'{b}호 우유 배달 중지x')
        else:
            print(f'{b}호 우유 배달 계속o')









