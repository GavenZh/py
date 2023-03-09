ch=input('请输入一行字符')
N=len(ch)
e=0
n=0
s=0
o=0
for i in range(0,N):
    if('a'<=ch[i]<='z' or 'A'<=ch[i]<='Z'):
        e+=1
    elif ('0'<=ch[i]<='9'):
        n+=1
    elif(ch[i]==' '):
        s+=1
    else : o+=1
print('该字符中包含的英文字符个数为：',e)
print('该字符中包含的数字字符个数为：',n)
print('该字符中包含的空格个数为：',s)
print('该字符中包含的其他字符个数为：',o)