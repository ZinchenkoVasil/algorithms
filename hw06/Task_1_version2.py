#4. Определить, какое число в массиве встречается чаще всего.

# Цель исследования
# в прошлой работе я измерил работу 2 вариантов алгоритма: реализация с словарем и "цикл в цикле"
# и пришел к выводу, что реализация с словарем работает быстрее
# в этой работе я хочу измерить расходы памяти и сравнить 2 варианта алгоритма
# в данном модуле будет исследован алгоритм "цикл в цикле"


import random
import show_size

def searchMax(lst):
    size_lst = show_size.show_size(lst)
    print("Размер начального списка: ", size_lst)
    print(f'type = {type(lst)}, size = {size_lst}')
    keys = set(lst)
    size_keys = show_size.show_size(keys)
    print("Размер множества из 1000 элементов: ", size_keys)
    print(f'type = {type(keys)}, size = {size_keys}')
    common_size = size_lst + size_keys
    print("Суммарный размер списка и множества: ", common_size)
    max_ = 0
    for key in keys:
        summ = 0
        for item in lst:
            if key == item:
                summ += 1
        if summ > max_:
            max_ = summ
            key_max = key
    return key_max

def main(n=10000):
    lst = [random.randint(1, 1000) for i in range(n)]
    return searchMax(lst)

main()

#Размер начального списка:  183816
#type = <class 'list'>, size = 183816
#Размер множества из 1000 элементов:  30500
#type = <class 'set'>, size = 30500
#Суммарный размер списка и множества:  214316

#список из 10000 элементов весит:  183816 байт
#множество из 1000 элементов весит: 30500 байт

#Вывод: отличия 2 алгоритмов по занимаемой памяти несущественны. Вариант "цикл в цикле" занимает немного меньше памяти.