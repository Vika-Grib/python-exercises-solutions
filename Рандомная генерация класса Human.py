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



import random
import datetime

class Human:
    male_names = ["Lionel McCoy", "Charles Cross", "John Pitz", "Jeffry Young", "Johnathan Randall", "Edward Townsend", "Lewis Pope"]
    female_names = ["Aubrey Gilmore", "Avice Reynolds", "Theresa Bradford", "Shonda Douglas", "Karen Sanders", "Ruby Rice", "Ruth Rice"]
    characters = ["холерик", "сангвиник", "меланхолик", "флегматик"]
    job_types = ["Рабочий", "Безработный"]
    marital_status = ["Свободен", "Женат/Замужем"]

    def __init__(self):
        self.gender = random.choice(["М", "Ж"])
        self.name = random.choice(self.male_names) if self.gender == "М" else random.choice(self.female_names)
        self.age = random.randint(18, 100)
        self.character = random.choice(self.characters)
        self.job = random.choice(self.job_types)
        self.capital = random.randint(100, 10000)
        self.income = random.randint(1000, 5000) if self.job == "Рабочий" else random.randint(100, 300)
        self.birth_date = self.generate_birth_date()
        self.death_date = self.generate_death_date()
        self.home = random.choice(["Свой дом", "Аренда"])
        self.car = random.choice(["Есть", "Нет"])
        self.marital_status = random.choice(self.marital_status)
        self.wedding_date = self.generate_wedding_date()

    def generate_birth_date(self):
        today = datetime.date.today()
        years_ago = datetime.timedelta(days=random.randint(18 * 365, self.age * 365))
        birth_date = today - years_ago
        return birth_date.strftime("%d.%m.%Y")

    def generate_death_date(self):
        today = datetime.date.today()
        years_ago = datetime.timedelta(days=random.randint(0, (100 - self.age) * 365))
        death_date = today + years_ago
        return death_date.strftime("%d.%m.%Y")

    def generate_wedding_date(self):
        if self.marital_status == "Свободен":
            birth_date = datetime.datetime.strptime(self.birth_date, "%d.%m.%Y").date()
            years_ago = datetime.timedelta(days=random.randint(18 * 365, self.age * 365))
            wedding_date = birth_date + years_ago
            return wedding_date.strftime("%d.%m.%Y")
        else:
            return None

    def info(self):
        print("Gender:", self.gender)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Character:", self.character)
        print("Job:", self.job)
        print("Capital:", self.capital)
        print("Income:", self.income)
        print("Birth Date:", self.birth_date)
        print("Death Date:", self.death_date)
        print("Home:", self.home)
        print("Car:", self.car)
        print("Marital Status:", self.marital_status)
        print("Wedding Date:", self.wedding_date)

    def life(self):
        if random.randint(1, 30) == 1:
            self.death_date = datetime.date.today().strftime("%d.%m.%Y")
        self.age += 1

    def find_job(self):
        if self.job == "Безработный":
            if self.character == "холерик":
                if random.randint(1, 2) == 1:
                    self.job = "Рабочий"
            elif self.character == "сангвиник":
                if random.randint(1, 3) == 1:
                    self.job = "Рабочий"
            elif self.character == "меланхолик":
                if random.randint(1, 7) == 1:
                    self.job = "Рабочий"
            elif self.character == "флегматик":
                if random.randint(1, 5) == 1:
                    self.job = "Рабочий"
        else:
            if random.randint(1, 7) == 1:
                self.job = "Безработный"

    def wedding(self):
        age = self.age
        if 18 <= age <= 30:
            if random.randint(1, 4) == 1:
                self.marital_status = "Женат/Замужем"
                self.wedding_date = datetime.date.today().strftime("%d.%m.%Y")
        elif 31 <= age <= 45:
            if random.randint(1, 7) == 1:
                self.marital_status = "Женат/Замужем"
                self.wedding_date = datetime.date.today().strftime("%d.%m.%Y")
        elif 46 <= age <= 65:
            if random.randint(1, 12) == 1:
                self.marital_status = "Женат/Замужем"
                self.wedding_date = datetime.date.today().strftime("%d.%m.%Y")
        elif age >= 66:
            if random.randint(1, 20) == 1:
                self.marital_status = "Женат/Замужем"
                self.wedding_date = datetime.date.today().strftime("%d.%m.%Y")

    def salary(self):
        if random.randint(1, 4) == 1:
            self.income = random.randint(1000, 5000)
        self.capital += self.income

    def expenses(self):
        expenses = self.income * 0.3
        if self.home == "Аренда":
            expenses *= 1.15
        else:
            expenses *= 1.07
        if self.car == "Есть":
            expenses *= 1.13
        self.capital -= expenses

    def house(self):
        if self.home != "Свой дом" and random.randint(1, 4) == 1:
            house_price = random.randint(20000, 50000)
            if self.capital >= house_price:
                self.capital -= house_price
                self.home = "Свой дом"

    def buy_car(self):
        if self.car != "Есть" and random.randint(1, 3) == 1:
            car_price = random.randint(5000, 100000)
            if self.capital >= car_price:
                self.capital -= car_price
                self.car = "Есть"


def select_human(humans):
    print("Выберите номер человека для получения информации:")
    for i, human in enumerate(humans):
        print(i, "-", human.name)
    choice = int(input("Ваш выбор (введите число от 0 до {}): ".format(len(humans) - 1)))
    if choice < 0 or choice >= len(humans):
        print("Неверный выбор")
        return None
    return humans[choice]

humans = [Human() for _ in range(random.randint(2, 5))]

years = 100
for year in range(years):
    # print("\nYear:", year + 1)
    for human in humans:
        human.life()
        human.find_job()
        human.wedding()
        human.salary()
        human.expenses()
        human.house()
        human.buy_car()

selected_human = select_human(humans)
if selected_human:
    print("\nInitial Information:")
    selected_human.info()

    print("\nEnd of Life Information:")
    selected_human.info()





# import random
# import datetime
#
# class Human:
#     male_names = [
#         "Lionel McCoy", "Charles Cross", "John Pitz", "Jeffry Young",
#         "Johnathan Randall", "Edward Townsend", "Lewis Pope"
#     ]
#     female_names = [
#         "Aubrey Gilmore", "Avice Reynolds", "Theresa Bradford",
#         "Shonda Douglas", "Karen Sanders", "Ruby Rice", "Ruth Rice"
#     ]
#     temperaments = ["холерик", "сангвиник", "меланхолик", "флегматик"]
#     job_statuses = ["Рабочий", "Безработный"]
#     house_statuses = ["Свой дом", "Аренда"]
#     car_statuses = ["Есть", "Нет"]
#     marital_statuses = {"Мужчина": "Женат", "Женщина": "Замужем"}
#
#     def __init__(self):
#         self.gender = random.choice(["Мужчина", "Женщина"])
#         self.name = random.choice(Human.male_names if self.gender == "Мужчина" else Human.female_names)
#         self.age = random.randint(18, 100)
#         self.temperament = random.choice(Human.temperaments)
#         self.job = random.choice(Human.job_statuses)
#         self.capital = random.randint(100, 10000)
#         self.income = random.randint(1000, 5000) if self.job == "Рабочий" else random.randint(100, 300)
#         self.birthdate = self._generate_random_date(years_ago=self.age)
#         self.deathdate = None
#         self.house_status = random.choice(Human.house_statuses)
#         self.car = random.choice(Human.car_statuses)
#         self.marital_status = "Свободен"
#         self.wedding_date = None
#         self.monthly_expenses = self.income * 0.3
#         self.jobs_count = 0 if self.job == "Рабочий" else None
#
#     def _generate_random_date(self, years_ago=0):
#         start_date = datetime.date.today().replace(year=datetime.date.today().year - years_ago)
#         end_date = start_date.replace(year=start_date.year + 1)
#         time_between_dates = end_date - start_date
#         random_number_of_days = random.randrange(time_between_dates.days)
#         return start_date + datetime.timedelta(days=random_number_of_days)
#
#     def info(self):
#         print(f"Name: {self.name}, Gender: {self.gender}, Age: {self.age}, Temperament: {self.temperament}, "
#               f"Job: {self.job}, Capital: ${self.capital}, Income: ${self.income}/month, "
#               f"House: {self.house_status}, Car: {self.car}, Marital Status: {self.marital_status}, "
#               f"Birthdate: {self.birthdate.strftime('%d.%m.%Y')}, "
#               f"Deathdate: {self.deathdate.strftime('%d.%m.%Y') if self.deathdate else 'N/A'}, "
#               f"Monthly Expenses: ${self.monthly_expenses}, Total Job Changes: {self.jobs_count}")
#
#     def life(self):
#         self.age += 1
#         if random.randint(1, 30) == 1 and not self.deathdate:
#             self.deathdate = datetime.date.today()
#             print(f"{self.name} has unexpectedly passed away at the age of {self.age}.")
#
#     def jobs(self):
#         get_job_chance = {"холерик": 0.5, "сангвиник": 0.33, "меланхолик": 0.14, "флегматик": 0.2}
#         lose_job_chance = {"холерик": 0.14, "сангвиник": 0.1, "меланхолик": 0.17, "флегматик": 0.05}
#         if self.job == "Безработный" and random.random() < get_job_chance[self.temperament]:
#             self.job = "Рабочий"
#             self.income = random.randint(1000, 5000)
#             self.jobs_count = (self.jobs_count or 0) + 1
#             print(f"{self.name} found a job.")
#         elif self.job == "Рабочий" and random.random() < lose_job_chance[self.temperament]:
#             self.job = "Безработный"
#             self.income = random.randint(100, 300)
#             self.jobs_count += 1
#             print(f"{self.name} lost their job.")
#
#     def wedding(self):
#         chances = {range(18, 31): 0.25, range(31, 46): 0.14, range(46, 66): 0.08, range(66, 101): 0.05}
#         for age_range, chance in chances.items():
#             if self.age in age_range and random.random() < chance and self.marital_status == "Свободен":
#                 self.marital_status = Human.marital_statuses[self.gender]
#                 self.wedding_date = self._generate_random_date()
#                 print(f"{self.name} got married.")
#
#     def salary(self):
#         self.capital += self.income - self.monthly_expenses
#         if random.random() < 0.25:
#             self.income = random.randint(1000, 5000)
#             print(f"{self.name}'s income has changed to ${self.income}/month.")
#
#     def expenses(self):
#         housing_expense_multiplier = 1.15 if self.house_status == "Аренда" else 1.07
#         car_expense_multiplier = 1.13 if self.car == "Есть" else 1
#         self.monthly_expenses = (self.income * 0.3) * housing_expense_multiplier * car_expense_multiplier
#
#     def house(self):
#         if self.house_status == "Аренда" and random.random() < 0.25:
#             house_price = random.randint(20000, 50000)
#             if self.capital >= house_price:
#                 self.capital -= house_price
#                 self.house_status = "Свой дом"
#                 print(f"{self.name} bought a house.")
#
#     def purchase_car(self):
#         if self.car == "Нет" and random.random() < 0.33:
#             car_price = random.randint(5000, 20000)
#             if self.capital >= car_price:
#                 self.capital -= car_price
#                 self.car = "Есть"
#                 print(f"{self.name} bought a car.")
#
#
# # Пример создания и использования объектов
# humans = [Human() for _ in range(random.randint(2, 5))]
#
# for year in range(1, 101):  # Примерный цикл жизни на 100 лет
#     print(f"Year: {year}")
#     for human in humans:
#         if not human.deathdate:  # Если человек ещё жив
#             human.life()
#             human.jobs()
#             human.wedding()
#             human.salary()
#             human.expenses()
#             human.house()
#             human.purchase_car()  # Обновленное имя метода
#     if all(human.deathdate for human in humans):  # Если все умерли
#         break
#
#
# # Вывод информации о каждом человеке
# for human in humans:
#     human.info()
