#4. Определить, какое число в массиве встречается чаще всего.

# Цель исследования
# Измерить работу 2 вариантов алгоритма: реализация с словарем и цикл в цикле
# в данном модуле будет исследован алгоритм "цикл в цикле"

import cProfile
import timeit
import random

def searchMax(lst):
    keys = set(lst)
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
    lst = [random.randint(1, 5) for i in range(n)]
    return searchMax(lst)


timeit.timeit("main()", number=3)
#n = 10000
#результаты запуска функции:
#50000000 loops, best of 5: 9.95 nsec per loop
#20000000 loops, best of 5: 9.91 nsec per loop
#20000000 loops, best of 5: 9.91 nsec per loop


cProfile.run("main(10000)")
#n = 10000
#результаты запуска функции при n = 10000 (n - количество элементов в массиве):
#55978 function calls in 0.024 seconds
#ncalls tottime percall cumtime percall filename: lineno(function)
#1       0.003    0.003   0.003   0.003 Task_1_version2.py:11(searchMax)

cProfile.run("main(100000)")
#n = 100000
#результаты запуска функции при n = 100000 (n - количество элементов в массиве):
#559579 function calls in 0.241 seconds
#ncalls tottime percall cumtime percall filename: lineno(function)
#1       0.025    0.025   0.025   0.025 Task_1_version2.py:11(searchMax)

cProfile.run("main(1000000)")
#n = 1000000
#результаты запуска функции при n = 1000000 (n - количество элементов в массиве):
#5601259 function calls in 2.471 seconds
#ncalls tottime percall cumtime percall filename: lineno(function)
#1       0.259    0.259   0.259   0.259 Task_1_version2.py:11(searchMax)


#Выводы:
# 1) общее время выполнения программы растет линейно с увеличением количества элементов массива
# линейная сложность O(n)
# 2) время выполнения функции createDist растет линейно с увеличением количества элементов массива O(n)
# линейная сложность O(n)

#Реализация этого алгоритма работает немного медленнее, так как приходится перебирать цикл в цикле,
#но поскольку в массиве всего 5 ключей первый цикл состоит из 5 элементов и разница получается несущественной
#необходимо дальнейшее сравнение обоих алгоритмов на 100 или 1000 ключах.
