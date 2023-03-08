# 成绩等级划分不包含89~90内之类的小数
while 1:
    x=eval(input("请输入成绩:"))
    if 90<=x<=100 :
        print('该成绩对应的等级为:A')
    elif 70<=x<=89 :
        print('该成绩对应的等级为:B')
    elif 60<=x<=69 :
        print('该成绩对应的等级为:C')
    elif 0<=x<=59 :
        print('该成绩对应的等级为:D')
    else :
        print('该成绩为无效成绩')
        break

