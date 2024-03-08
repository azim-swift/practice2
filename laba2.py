#Вариант 7. Натуральные числа.
#Выводит на экран числа, содержащие хотя бы одну последовательность длиннее К подряд идущих одинаковых цифр. 
#Рядом с таким числом выводится повторяющаяся цифра (прописью) и количество повторений.

import re

def convert_number_to_words(number):
    words_dict = {
        '0': 'нуль',
        '1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'четыре',
        '5': 'пять',
        '6': 'шесть',
        '7': 'семь',
        '8': 'восемь',
        '9': 'девять'
    }
    return ' '.join([words_dict[digit] for digit in str(number)])

def find_regular_numbers(k):
    regular_numbers = []
    for number in range(1, 10000):
        number_str = str(number)
        matches = re.findall(r'(\d)\1{%d,}' % k, number_str)
        if matches:
            for match in matches:
                repetitions = len(match)
                number_words = convert_number_to_words(match[0])
                regular_numbers.append((number, number_words, repetitions))
    return regular_numbers

# тест
k = int(input('Введите K: '))
regular_numbers = find_regular_numbers(k)

for number, number_words, repetitions in regular_numbers:
    print(f"Число: {number}, Повторяющаяся цифра: {number_words}, Количество повторений: {repetitions}")
