# HWsetlotto

# while~while ~ if ~ else

import random

def mysetlotto():
    print('로또 추첨 START!')

    lotto = set()
    # while~while ~ if ~ else

    # 로또 번호 생성
    while len(lotto) < 6 :
        num = random.randint(1,45)
        # 중복 체크 후 번호 추가
        if num not in lotto :   # 중복 체크
            lotto.add(num)      # 번호 추가
    # set 정렬
    sorted_lotto = sorted(list(lotto))  # 오름차순

    print('추첨 번호: ', sorted_lotto)

mysetlotto()