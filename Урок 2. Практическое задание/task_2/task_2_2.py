"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recfunc(num, chet=0, nechet=0):
    """ Наша рекурсия"""

    if num == 0:
        return chet, nechet
    else:
        # достаем очередную цифру числа
        cif = num % 10
        # число естественно становится короче
        num = num // 10
        # проверяем цифра четная или нечетная
        if cif % 2 == 0:
            chet += 1
            return recfunc(num, chet, nechet)
        else:
            nechet += 1
            return recfunc(num, chet, nechet)


try:
    NUMB = int(input("Введите число: "))
    print(f"Количество четных и нечетных цифр в числе: {recfunc(NUMB)}")
except ValueError:
    print("Введите число. Попробуйте еще раз.")

