n, flag, s = 10, 1, 0
for i in range(1, n + 1):
    flag = flag * i
    s = s + flag
    print(f'{flag}+', sep='', end='')
print(f'\b={s}', sep='', end='')
