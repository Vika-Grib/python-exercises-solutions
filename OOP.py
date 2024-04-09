# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)


class Tomato:
    # разные стадии созревания томатов
    states = {'none': 0, 'flower':1, 'green': 2, 'red': 3}

    def __init__(self, index):
        self._index = index   # _index - передается параметром
        self._state = self.states['none'] #_state - принимает первое значение из словаря states

    def grow(self):
        if self._state < 3:  # если не созрел, то +1 к каждой стадии созревания пока не станет красным и спелым
            self._state += 1

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая


class TomatoBush:
    def __init__(self, num):  # num - количество помидоров, которые мы будем выращивать и проверять стадии
        self.tomatoes = [Tomato(i) for i in range(num)]
        print(self.tomatoes)

    def grow_all(self):
        for each_tomato in self.tomatoes:
            each_tomato.grow()

    def all_are_ripe(self):
        for each_tomato in self.tomatoes:
            each_tomato.is_ripe()  # проверяем все ли помидоры созрели


    def give_away_all(self):
        self.tomatoes = []  # весь урожай собрали и теперь список снова пустой для нового урожая

# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник начинает свою работу, что позволит растению стать более зрелым.')
        self._plant.grow_all()  #садовник вызывает метод чтобы созрели все томаты
        print('Садовник закончил свою работу.')

    def harvest(self):
        print('Начинаем собирать урожай!')
        # проверяем если все созрели - то собираем нашим методом give_away_all(self)
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай собран')
        else:
            print('Еще рано. Не все помидоры созрели!')



# Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.

    @staticmethod
    def for_exam():
        print('Решаем задачу по выращиванию помидоров')

Gardener.for_exam()

#Создайте объекты классов TomatoBush и Gardener
obj_tomatoBush = TomatoBush(2)
obj_gardener = Gardener('Иван', obj_tomatoBush)

# Используя объект класса Gardener, поухаживайте за кустом с помидорами
obj_gardener.work()
obj_gardener.work()
obj_gardener.harvest()

#  Если томаты еще не дозрели, продолжайте ухаживать за ними
#  Соберите урожай

obj_gardener.work()
obj_gardener.harvest()