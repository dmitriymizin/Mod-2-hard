

def counting():
    num_ = int(input('Введите число от 3 до 20: '))
    list_ = []
    list_2 = set()
    for i in range(1, num_ + 1):
        for j in range(1, num_ + 1):
            if i == j:
                continue
            if num_ % (i + j) == 0 and (i, j) not in list_2:
                list_.append(i)
                list_.append(j)
                list_2.add((i,j))
                list_2.add((j,i))
    print(num_, '-',*list_, sep='')

counting()

