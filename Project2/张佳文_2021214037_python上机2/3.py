x=int(input('请输入一个五位的自然数：'))
if(x<10000 or 99999<=x):
    exit('输入错误')
a=x%10
b=int((x/10))%10
c=int((x/100))%10
d=int((x/1000))%10
e=int((x/10000))%10
if(a==e and b==d):
    print('该数是回文数')
else: print('该数不是回文数')


