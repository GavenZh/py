# 汉诺塔问题描述为如何将所有盘子从A移动到C（借助B），请编写一个汉诺塔的移动函数，采用递归方式解决。输入是汉诺塔的层数，输出是完整的移动过程。
def move(x, a, b, c):
    if x == 1:
        print(a, '--->', c, sep=' ', end="\n")
    else:
        move(x - 1, a, c, b)
        move(1, a, b, c)
        move(x - 1, b, a, c)


n = int(input('请输入汉诺塔的层数'))
move(n, 'A', 'B', 'C')
