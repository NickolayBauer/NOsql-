def create(name):
    return [name]


def add(table, *args):
    table.append(*args)


def show(table):
    for i in table:
        print(i)


def select_id(table, i):
    return str(table[0] + '\n' + table[1] + '\n' + table[i - 1])


def select_were(table, sys, row):
    ls = []
    for i in range(2, len(table)):
        if row == '*':
            ls.append(table[i])
        elif table[i][table[1].index(sys)] == row:
            ls.append(table[i])
    return ls


def sortd(table, param):
    ls = []

    for i in range(2, len(table)):
        ls.append(table[i])
    ls = sorted(ls, key=lambda row: row[table[1].index(param)])
    ls.insert(0, table[0])
    ls.insert(1, table[1])
    return ls


table = create('Персонажи')
add(table, ['Имя', 'Игра'])
add(table, ['Геральт', 'Ведьмак III'])
add(table, ['Аджай', 'Far Cry IV'])
add(table, ['Артём', 'Метро 2033'])
add(table, ['Хантер', 'Метро 2033'])
# show(table)

print('this_is_select:', select_were(table, 'Игра', 'Ведьмак III'))
print(sortd(table, 'Имя'))
