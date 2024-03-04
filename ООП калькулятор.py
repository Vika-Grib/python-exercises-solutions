class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Ошибка: Деление на ноль"

    def get_data(self):
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        operation = input("Введите операцию (+, -, *, /): ")

        if operation == '+':
            print("Результат:", self.add(a, b))
        elif operation == '-':
            print("Результат:", self.subtract(a, b))
        elif operation == '*':
            print("Результат:", self.multiply(a, b))
        elif operation == '/':
            print("Результат:", self.divide(a, b))
        else:
            print("Неизвестная операция")
calc = Calculator()
calc.get_data()