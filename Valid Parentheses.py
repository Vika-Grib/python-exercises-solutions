"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
 1. Open brackets must be closed by the same type of brackets.
 2. Open brackets must be closed in the correct order.
 3. Every close bracket has a corresponding open bracket of the same type."""


def isValid(s: str) -> bool:
    # Инициализация стека
    stack = []

    # Словарь соответствий закрывающих и открывающих скобок
    brackets = {')': '(', '}': '{', ']': '['}

    for sym in s:
        if sym in brackets.values():
            stack.append(sym)
        elif sym in brackets.keys():
            if len(stack) == 0 or brackets[sym] != stack.pop():
                print('not correct')
                return
    else:
        if len(stack) > 0:
            print('not correct')
        else:
            print('correct')

# Примеры использования
isValid("()[]{}")  # correct
isValid("([)]")    # not correct
isValid("{[]}")    # correct
