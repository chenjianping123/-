TemStr = eval(input("qingshurudaiyfuhaodewenduzhi"))
while TemStr[-1] not in ['N','n']:
    if TemStr[-1] in ['F','f']:
        c = (eval(TemStr[0:-1])-32)/1.8
        print("zhuanhuanwendushi{:.2f}c".format(c))
    elif TemStr[-1] in ['C','c']:
        F = 1.8*eval(TemStr[0:-1]) + 32
    print("zhuanhuanhouwendu{:.2f}F".format(F))
else:
    print("qingshurugshicuowu")
TemStr = input("qingshuru:")
