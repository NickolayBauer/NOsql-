class Table:
    def __init__(self, name, *args):
        self.name = name
        data = []
        self.data = data
        system = []
        for arg in args:
            system.append(arg)
        self.system = system

    def apnd(self, *args):

        if len(args) != len(self.system):
            print('ашыпка')
        else:
            self.data.append(args)

    def show_me_all(self):

        print(self.name + '\n' + str(self.system))
        for row in self.data:
            print(row)

    def select(self, chrome, xde):
        ls = []

        for row in self.data:
            if row[self.system.index(chrome)] == xde:
                ls.append(row)

        return ls

    def sortd(self, param):
        return sorted(self.data, key=lambda row: row[self.system.index(param)])


my_par = Table('Таблица один', *['Имя', 'Игра'])
my_par.apnd(*['Артём', 'Метро'])
my_par.apnd(*['Хантер', 'Метро'])
my_par.apnd(*['Пейган', 'Far cry'])
my_par.apnd(*['Геральт', 'Ведьмак'])
my_par.show_me_all()
print('_____________________________')
print(my_par.select('Игра', 'Метро'))
print(my_par.sortd('Имя'))
