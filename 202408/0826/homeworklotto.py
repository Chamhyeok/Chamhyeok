# homeworklotto.py

import random

lotto = []


while True :
    com = random.randint(1,45)
    if com in lotto:
        continue
    lotto.append(com)

    if len(lotto) == 6:
        break

lotto.sort()
for k in lotto:
    print(k, end = ' ')






















