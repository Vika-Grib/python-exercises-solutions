'''***6. Напишите программу, которая будет рандомно генирировать от 2 до 5 объектов класса Human.
У каждого объекта этого класса рандомным образом должны определяться следующие свойства:
1) Пол: Мужчина или Женщина
2) Рандомное имя в зависимости от пола:
М(Lionel McCoy, Charles Cross, John Pitz, Jeffry Young, Johnathan Randall, Edward Townsend, Lewis Pope)
Ж(Aubrey Gilmore, Avice Reynolds, Theresa Bradford, Shonda Douglas, Karen Sanders, Ruby Rice, Ruth Rice)
Можно дополнить своими вариантами
3) Возраст: от 18 до 100 лет
4) Характер: холерик или сангвиник или меланхолик или флегматик
5) Место работы: Рабочий или Безработный
6) Рандомный капитал от 100$ до 10000$
7) Рандомный ежемесячный доход от 1000$ до 5000$, при наличии работы. Если работы нет, то от 100$ до 300$.
8) Рандомная дата рождения в формате xx.xx.xxxx(тип Private)
9) Рандомная дата смерти в формате xx.xx.xxxx(тип Private)
10) Наличие дома: Свой дом или Аренда
11) Наличие машины: Есть или нет
12) Семейное положение: Свободен или Женат/Замужем в зависимости от пола
13) Дата свадьбы, если статус Женат/Замужем присвоен сразу, то рандомная дата
в формате xx.xx.xxxx(тип Protected) в диапазоне от даты рождения +18 лет до текущего возраста
Если изначально статус свободен, то значение None
14) Ежемесячные расходы 30% от ежемесячного дохода

Создать метод info() с информацией о каждом объекте класса Human

Создать метод life() который ежегодно(1 итерация цикла) будет прибылвять 1 год объекту класса Human
Добавить шанс 1/30, что жизнь может оборваться преждевременно, в таком случае изменить дату смерти

Создать метод jobs() который ежегодно(1 итерация цикла) будет определять появиться ли работа у того,
у кого ее не было, или уволят ли того, у кого работа была и перезавписывать это свойство объекта.
Если характер "холерик", то шансы устроиться на работу 1/2, шансы быть уволеным 1/7
Если характер "сангвиник", то шансы устроиться на работу 1/3, шансы быть уволеным 1/10
Если характер "меланхолик", то шансы устроиться на работу 1/7, шансы быть уволеным 1/6
Если характер "флегматик", то шансы устроиться на работу 1/5, шансы быть уволеным 1/20
Добавить счётчик, который посчитает кол-во работ за всю жизнь.

Создать метод wedding() который ежегодно(1 итерация цикла) будет определять появиться ли вторая
половинка, если ее не было. От 18 до 30 лет шансы 1/4, от 31 до 45 шансы 1/7,
от 46 до 65 шансы 1/12, от 66+ шансы 1/20
Метод должен перезаписывать дату свадьбы

Создать метод salary() который ежегодно будет увеличивать капитал объекта согласно его доходу.
Добавить шанс 1/4 что доход может измениться в рандом диапазоне от 1000$ До 5000$.

Создать метод expenses() который ежегодно будет отнимать расходы от капитала
При наличии арендного жилья расходы должны увеличиваться на 15%, при собственном жилье только на 7%
При наличии авто расходы должны увеличиваться на 13%

Создать метод house() который ежегодно с шансом 1/4 будет определять, появиться ли у обекта свой
дом, если его еще не было при условии, что у объекта будет нужная сумма и отнимать от капитала
цену дома при покупке. Цена дома генирируется рандомно каждый год от 20000$ до 50000$

Создать метод car() который ежегодно с шансом 1/3 будет определять, появиться ли у обекта своя
машина, если ее еще не было при условии, что у объекта будет нужная сумма и отнимать от капитала
цену машины при покупке. Цена машины генирируется рандомно каждый год от 5000$ до 100000$


Как только все объекты умрут, добавить возможность выбора о каком объекте вывести информацию
на экран. Информация должна быть сначала изначальной, потом на конец жизни, чтобы можно было
сравнить данные.'''

# -*- coding: utf-8 -*-
import random
import copy


class Human:
    current_year = 2024
    names_m = ['Lionel McCoy', 'Charles Cross', 'John Pitz', 'Jeffry Young', 'Johnathan Randall', 'Edward Townsend',
               'Lewis Pope']
    names_w = ['Aubrey Gilmore', 'Avice Reynolds', 'Theresa Bradford', 'Shonda Douglas', 'Karen Sanders', 'Ruby Rice',
               'Ruth Rice']

    def __init__(self):
        self.male = random.choice(['М', 'Ж'])
        self.name = random.choice(self.names_m) if self.male == 'М' else random.choice(self.names_w)
        self.age = random.randint(18, 100)
        self.character = random.choice(['холерик', 'сангвиник', 'меланхолик', 'флегматик'])
        self.job = random.choice(['Рабочий', 'Безработный'])
        self.capital = random.randint(100, 10000)
        self.income = random.randint(1000, 5000) if self.job == 'Рабочий' else random.randint(100, 300)
        self.__birthday = self.gen_birthday()
        self.__deathday = self.gen_deathday()
        self.home = random.choice(('Свой дом', 'Аренда'))
        self.car = random.choice(('Своя машина', 'Нет машины'))
        self.famaly = random.choice(('Свободен', 'Женат' if self.male == 'М' else 'Замужем'))
        self._wedding_day = None if self.famaly == 'Свободен' else self.gen_weddingday()
        self.spend = round(self.income * 0.3, 2)

    def gen_birthday(self):
        day = random.randint(1, 29)
        mounth = random.randint(1, 12)
        year = self.current_year - self.age
        return f'{f"0{day}" if day < 10 else day}.{f"0{mounth}" if mounth < 10 else mounth}.{year}'

    def gen_deathday(self):
        day = random.randint(1, 29)
        mounth = random.randint(1, 12)
        year = random.randint(self.current_year, self.current_year + 100 - self.age)
        return f'{f"0{day}" if day < 10 else day}.{f"0{mounth}" if mounth < 10 else mounth}.{year}'

    def gen_weddingday(self):
        day = random.randint(1, 29)
        mounth = random.randint(1, 12)
        year = random.randint(int(self.__birthday[-4:]) + 18, self.current_year)
        return f'{f"0{day}" if day < 10 else day}.{f"0{mounth}" if mounth < 10 else mounth}.{year}'

    def info(self):
        return f'Пол: {self.male}\nИмя: {self.name}\nВозраст: {self.age}\nХарактер:{self.character}\nДата Рождения: {self.__birthday}\nДата смерти: {self.__deathday}\nНаличие дома: {self.home}\nНаличие машины: {self.car}\nСемейное положение: {self.famaly}\nДата свадьбы: {self._wedding_day}\nНаличие работы: {self.job}\nДоход: {self.income}$\nРасходы: {self.spend}$\nКапитал: {round(self.capital, 2)}$'

    def life(self):
        self.age += 1
        self.current_year += 1
        self.work()
        self.salary()
        self.expenses()
        if self.famaly == 'Свободен':
            self.wedding()
        self.win_car()
        self.house()
        self.__deathday = self.__deathday if random.randint(0, 29) else self.gen_deathday()

    def work(self):
        dict_workchances = {"холерик": {'Безработный': (0, 1), 'Рабочий': (0, 6)},
                            "сангвиник": {'Безработный': (0, 2), 'Рабочий': (0, 9)},
                            "меланхолик": {'Безработный': (0, 6), 'Рабочий': (0, 5)},
                            "флегматик": {'Безработный': (0, 4), 'Рабочий': (0, 19)}}
        if self.job == 'Безработный':
            self.job = self.job if random.randint(*dict_workchances[self.character][self.job]) else 'Рабочий'
        else:
            self.job = self.job if random.randint(*dict_workchances[self.character][self.job]) else 'Безработный'

    def wedding(self):
        dict_weddingchances = {x: (0, 3) if x <= 30 else ((0, 6) if x <= 45 else ((0, 11) if x <= 65 else (0, 19))) for
                               x in range(18, 100)}

        if self.male == 'М':
            self.famaly = self.famaly if random.randint(*dict_weddingchances[self.age]) else 'Женат'
        else:
            self.famaly = self.famaly if random.randint(*dict_weddingchances[self.age]) else 'Замужем'

    def salary(self):
        if random.randint(0, 3):
            self.income = random.randint(1000, 5000) if self.job == 'Рабочий' else random.randint(100, 300)
        self.capital += self.income

    def expenses(self):
        self.capital -= (self.spend + (self.income * 0.15 if self.home == 'Аренда' else self.income * 0.07) + (
            self.income * 0.13 if self.car == 'Своя машина' else 0))

    def house(self):
        # if self.home == 'Аренда' and random.random(0, 2) == 0 and self.capital >= (house_price := random.randint(20000, 50000)):
        # if self.home == 'Аренда' and random.random() < 0,25 and self.capital >= (house_price := random.randint(20000, 50000)):
        if self.home == 'Аренда' and random.random() < 1 / 4 and self.capital >= (house_price := random.randint(20000, 50000)):
            self.capital -= house_price
            self.home = 'Свой дом'


    def win_car(self):
        if self.car == 'Нет машины' and random.random() < 1/3 and self.capital >= (car_price := random.randint(5000, 100000)):
            self.capital -= car_price
            self.car = 'Своя машина'

    # def win_car(self):
    #     if self.car == 'Нет машины':
    #         if random.random() < 1 / 3:
    #             car_price = random.randint(5000, 100000)
    #             if self.capital >= car_price:
    #                 self.capital -= car_price
    #                 self.car = 'Своя машина'


    # def win_car(self):
    #     if self.car == 'Нет машины' and random.randint(0, 2) == 0 and self.capital >= (car_price := random.randint(5000, 100000)):
    #         self.capital -= car_price
    #         self.car = 'Своя машина'




humans = [Human() for _ in range(random.randint(2, 5))]
humans_live = copy.deepcopy(humans)
humans_death = []
while humans_live:
    for human in humans_live:
        while human.current_year != int(human._Human__deathday[-4:]):
            human.life()
        else:
            humans_live.remove(human)
            humans_death.append(human)

while True:
    print('Информацию о ком вы хотите получить?')
    for n, human in enumerate(humans_death):
        print(f'{n + 1} - {human.name}')
    choice = int(input('Введите: '))
    print(humans[choice - 1].info())
    print()
    print(humans_death[choice - 1].info())






# import random
# import datetime
#
# class Human:
#     male_names = ["Lionel McCoy", "Charles Cross", "John Pitz", "Jeffry Young", "Johnathan Randall", "Edward Townsend", "Lewis Pope"]
#     female_names = ["Aubrey Gilmore", "Avice Reynolds", "Theresa Bradford", "Shonda Douglas", "Karen Sanders", "Ruby Rice", "Ruth Rice"]
#     characters = ["холерик", "сангвиник", "меланхолик", "флегматик"]
#     job_types = ["Рабочий", "Безработный"]
#     marital_status = ["Свободен", "Женат/Замужем"]
#
#     def __init__(self):
#         self.gender = random.choice(["М", "Ж"])
#         self.name = random.choice(self.male_names) if self.gender == "М" else random.choice(self.female_names)
#         self.age = random.randint(18, 100)
#         self.character = random.choice(self.characters)
#         self.job = random.choice(self.job_types)
#         self.capital = random.randint(100, 10000)
#         self.income = random.randint(1000, 5000) if self.job == "Рабочий" else random.randint(100, 300)
#         self.birth_date = self.generate_birth_date()
#         self.death_date = self.generate_death_date()
#         self.home = random.choice(["Свой дом", "Аренда"])
#         self.car = random.choice(["Есть", "Нет"])
#         self.marital_status = random.choice(self.marital_status)
#         self.wedding_date = self.generate_wedding_date()
#
#     def generate_birth_date(self):
#         today = datetime.date.today()
#         years_ago = random.randint(0, 100)  # Генерируем случайное количество лет от 0 до self.age
#         birth_date = today.replace(year=today.year - years_ago)  # Вычитаем случайное количество лет из текущего года
#         return birth_date.strftime("%d.%m.%Y")  # strftime(format) для форматирования объекта даты в строку с определенным форматом
#
#
#     def generate_death_date(self):
#         today = datetime.date.today()
#         years_ago = datetime.timedelta(days=random.randint(0, (100 - self.age) * 365))
#         death_date = today + years_ago
#         return death_date.strftime("%d.%m.%Y")
#
#     def generate_wedding_date(self):
#         if self.marital_status == "Свободен":
#             birth_date = datetime.datetime.strptime(self.birth_date, "%d.%m.%Y").date()
#             years_ago = datetime.timedelta(days=random.randint(18 * 365, self.age * 365))
#             wedding_date = birth_date + years_ago
#             return wedding_date.strftime("%d.%m.%Y")
#         else:
#             return None
#
#     def info(self):
#         print("Gender:", self.gender)
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Character:", self.character)
#         print("Job:", self.job)
#         print("Capital:", self.capital)
#         print("Income:", self.income)
#         print("Birth Date:", self.birth_date)
#         print("Death Date:", self.death_date)
#         print("Home:", self.home)
#         print("Car:", self.car)
#         print("Marital Status:", self.marital_status)
#         print("Wedding Date:", self.wedding_date)
#
#     def life(self):
#         if random.randint(1, 30) == 1:
#             self.death_date = datetime.date.today().strftime("%d.%m.%Y")
#         self.age += 1
#
#     def find_job(self):
#         if self.job == "Безработный":
#             if self.character == "холерик":
#                 if random.randint(1, 2) == 1:
#                     self.job = "Рабочий"
#             elif self.character == "сангвиник":
#                 if random.randint(1, 3) == 1:
#                     self.job = "Рабочий"
#             elif self.character == "меланхолик":
#                 if random.randint(1, 7) == 1:
#                     self.job = "Рабочий"
#             elif self.character == "флегматик":
#                 if random.randint(1, 5) == 1:
#                     self.job = "Рабочий"
#         else:
#             if random.randint(1, 7) == 1:
#                 self.job = "Безработный"
#
#     def wedding(self):
#         age = self.age
#         if 18 <= age <= 30:
#             if random.randint(1, 4) == 1:
#                 self.marital_status = "Женат/Замужем"
#                 self.wedding_date = datetime.date.today().strftime("%d.%m.%Y")
#         elif 31 <= age <= 45:
#             if random.randint(1, 7) == 1:
#                 self.marital_status = "Женат/Замужем"
#                 self.wedding_date = datetime.date.today().strftime("%d.%m.%Y")
#         elif 46 <= age <= 65:
#             if random.randint(1, 12) == 1:
#                 self.marital_status = "Женат/Замужем"
#                 self.wedding_date = datetime.date.today().strftime("%d.%m.%Y")
#         elif age >= 66:
#             if random.randint(1, 20) == 1:
#                 self.marital_status = "Женат/Замужем"
#                 self.wedding_date = datetime.date.today().strftime("%d.%m.%Y")
#
#     def salary(self):
#         if random.randint(1, 4) == 1:
#             self.income = random.randint(1000, 5000)
#         self.capital += self.income
#
#     def expenses(self):
#         expenses = self.income * 0.3
#         if self.home == "Аренда":
#             expenses *= 1.15
#         else:
#             expenses *= 1.07
#         if self.car == "Есть":
#             expenses *= 1.13
#         self.capital -= expenses
#
#     def house(self):
#         if self.home != "Свой дом" and random.randint(1, 4) == 1:
#             house_price = random.randint(20000, 50000)
#             if self.capital >= house_price:
#                 self.capital -= house_price
#                 self.home = "Свой дом"
#
#     def buy_car(self):
#         if self.car != "Есть" and random.randint(1, 3) == 1:
#             car_price = random.randint(5000, 100000)
#             if self.capital >= car_price:
#                 self.capital -= car_price
#                 self.car = "Есть"
#
#
# def select_human(humans):
#     print("Выберите номер человека для получения информации:")
#     for i, human in enumerate(humans):
#         print(i, "-", human.name)
#     choice = int(input("Ваш выбор (введите число от 0 до {}): ".format(len(humans) - 1)))
#     if choice < 0 or choice >= len(humans):
#         print("Неверный выбор")
#         return None
#     return humans[choice]
#
# humans = [Human() for _ in range(random.randint(2, 5))]
#
# years = 100
# for year in range(years):
#     # print("\nYear:", year + 1)
#     for human in humans:
#         human.life()
#         human.find_job()
#         human.wedding()
#         human.salary()
#         human.expenses()
#         human.house()
#         human.buy_car()
#
# selected_human = select_human(humans)
# if selected_human:
#     print("\nInitial Information:")
#     selected_human.info()
#
#     print("\nEnd of Life Information:")
#     selected_human.info()


