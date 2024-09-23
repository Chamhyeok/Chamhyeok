# homeworkdic.py

# 가나다, 라마바, 사아자, 차카타

score_dic = {
    '가나다': [100, 82],
    '라마바': [90, 68],
    '사아자': [80, 88],
    '차카타': [90, 74]
    }

# 가나다 182 91
# 라마바 158 79
# 사아자 168 84
# 차카타 164 82


for key in score_dic:
    print(key,':', sum(score_dic[key]), sum(score_dic[key])//len(score_dic[key]))









