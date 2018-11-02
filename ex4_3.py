a,b = eval(input("请输入两个整数，中间以逗号隔开:"))
x,y = a,b
r = a % b
while r != 0:
    a,b = b,r
    r = a % b

print("{}和{}的最大公约数：{};最小公倍数：{:.0f}".format(x,y,b,x*y/b))
