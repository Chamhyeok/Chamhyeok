# 14sort

a=[4,7,5,1,2];
for i in range(4): # 처음 기준되는 숫자
    for j in range(i,5): #비교대상
        if a[i]>a[j] :
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
    print(a)