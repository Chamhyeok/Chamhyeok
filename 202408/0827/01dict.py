# 01dict

a_list = ['LEE', 98.85, False] # list 선언
a_dict = {} # dict 선언

a_dict[5] = 'Kyoto'     # dict[key] = 'value'
a_dict[6] = 'Osaka'
a_dict[7] = 'Tokyo'

for k,v in a_dict.items():
    print(k, ':', v)

print()
for i,k in enumerate(a_dict):
    print((i+1), "", k, a_dict[k])