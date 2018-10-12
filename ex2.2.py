#2.2人名币和美元转换.py
money = input("请输入带有符号的人民币种:")
if money[-1] in ['y','Y']:
    M=6*eval(money[:-1])
    print("兑换后的金钱是{:.2f}D".format(M))
if money[-1] in ['d','D']:
    M=eval(money[:-1])/6
    print("兑换后的金钱是{:.2f}D".format(M))
else:
    print("输入格式错误")
money = input("请输入带有符号的币种:")
    
