#версия PYTHON: Python 3.7.0
#64-разрядная Операционная система

#4. Определить, какое число в массиве встречается чаще всего.


# Цель исследования
# в прошлой работе я измерил работу 2 вариантов алгоритма: реализация с словарем и "цикл в цикле"
# и пришел к выводу, что реализация с словарем работает быстрее.
# В этой работе я хочу измерить расходы памяти и сравнить 2 варианта алгоритма по расходам памяти!
# в данном модуле будет исследован алгоритм с словарем

import random
import show_size

def createDist(lst):
    dubl = {}
    for i in lst:
        if i in dubl:
            dubl[i] += 1
        else:
            dubl[i] = 1
    return dubl
def searchMax(dubl):
    max_ = 0
    for key in dubl:
        if dubl[key] > max_:
            max_ = dubl[key]
            key_max = key
    return key_max

def main(n=10000):
    lst = [random.randint(1, 1000) for i in range(n)]
    size_lst = show_size.show_size(lst)
    print("Размер начального списка: ", size_lst)
    print(f'type = {type(lst)}, size = {size_lst}')

    dubl = createDist(lst)
    size_dubl = show_size.show_size(dubl)
    print("Размер результирующего словаря из 1000 элементов: ", size_dubl)
    print(f'type = {type(dubl)}, size = {size_dubl}')
    common_size = size_lst + size_dubl
    print("Суммарный размер списка и словаря: ", common_size)
    return searchMax(dubl)

main()

#Размер начального списка:  183816
#type = <class 'list'>, size = 183816
#Размер результирующего словаря из 1000 элементов:  48544
#type = <class 'dict'>, size = 48544
#Суммарный размер списка и словаря:  232360

#список из 10000 элементов весит: 183816 байт
#словарь из 1000 элементов весит:  48544 байт  (примерно в 4 раза меньше, чем список из 10 000 элементов)




