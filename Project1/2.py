x = int(input('请输入一个正整数:'))
if x <= 0:
    print('输入错误')
else:
    flag = 2
    print(x, "的质因数为x=", sep='', end='')
    while flag <= x:
        if x % flag == 0 and (not flag == x):
            print(flag, end='*')
            x = x / flag
        elif flag == x:
            print(flag, end=' ')
            break
        else:
            flag += 1
