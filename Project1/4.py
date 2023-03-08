flag = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and j != k and i != k:
                print(f'{i}{j}{k}', end=" ")
                flag += 1
print(f'一共有{flag}个')
