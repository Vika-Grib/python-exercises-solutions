'''ООП ДЕКОРАТОРЫ'''
class Class1:

    def __init__(self, value):
        self.__var = value

    @property
    def read_set_del(self):
        print('Прочтено')
        return self.__var

    @read_set_del.setter
    def read_set_del(self, value):
        self.__var = value
        print('Изменено')

    @read_set_del.deleter
    def read_set_del(self):
        del self.__var
        print('Удалено')

c1 = Class1(5)
c1.read_set_del = 35
c1.read_set_del
del c1.read_set_del

