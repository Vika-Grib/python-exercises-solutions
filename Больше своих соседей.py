'''Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей и выведите количество таких элементов.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода
Выведите ответ на задачу.'''


x = list(map(int, input().split()))

def check_list(x: list):
    counter = 0
    if len(x) < 3:
        return counter
    more_left = x[1] > x[0]
    for i in range(1, len(x)-1):
        more_right = x[i] > x[i+1]
        if more_left and more_right:
            counter += 1
        more_left = not more_right
    return counter

print(check_list(x))