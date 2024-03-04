'''Два метода в классе, один принимает в себя либо строку, либо число.

Если передают строку, то смотрим:
если произведение гласных и согласных букв меньше или равно
длине слова, выводить все гласные, иначе согласные;
Если передают число то находим, произведение суммы чётных цифр на длину числа.

Длину строки и числа искать во втором методе'''

#Этот класс StringNumberProcessor имеет два метода: _process_string() и _process_number(),
# которые выполняют операции в зависимости от типа входных данных.
# Метод process_input() определяет тип данных и вызывает соответствующий метод для обработки входных данных.

class StringNumberProcessor:
    def __init__(self):
        pass

    def process_input(self, data):
        if isinstance(data, str):
            return self._process_string(data)
        elif isinstance(data, int):
            return self._process_number(data)
        else:
            return "Unsupported data type"

    def _process_string(self, data):
        vowels = "aeiouAEIOU"
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

        vowels_count = sum(1 for char in data if char in vowels)
        consonants_count = sum(1 for char in data if char in consonants)

        if vowels_count * consonants_count <= len(data):
            return "".join(char for char in data if char in vowels)
        else:
            return "".join(char for char in data if char in consonants)

    def _process_number(self, data):
        digits = [int(digit) for digit in str(data)]
        even_sum = sum(digit for digit in digits if digit % 2 == 0)
        return even_sum * len(digits)

# Пример использования:
processor = StringNumberProcessor()
print(processor.process_input("Hello"))  # Output: eoo
print(processor.process_input(12345))    # Output: 36
