#4. Определить, какое число в массиве встречается чаще всего.

# Цель исследования
# Измерить работу 2 вариантов алгоритма: реализация с словарем и цикл в цикле
# в данном модуле будет исследован алгоритм с словарем

import cProfile
import timeit
import random

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
    lst = [random.randint(1, 5) for i in range(n)]
    dubl = createDist(lst)
    return searchMax(dubl)

timeit.timeit("main()", number=3)
#n = 10000
#результаты запуска функции:
#20000000 loops, best of 5: 10.6 nsec per loop
#20000000 loops, best of 5: 9.84 nsec per loop
#20000000 loops, best of 5: 10.6 nsec per loop


cProfile.run("main(10000)")
#n = 10000
#результаты запуска функции при n = 10000 (n - количество элементов в массиве):
#55992 function calls in 0.023 seconds
#ncalls tottime percall cumtime percall filename: lineno(function)
#1       0.001    0.001   0.001   0.001 Task_1.py:6(createDist)

cProfile.run("main(100000)")
#n = 100000
#результаты запуска функции при n = 100000 (n - количество элементов в массиве):
#560121 function calls in 0.230 seconds
#ncalls tottime percall cumtime percall filename: lineno(function)
#1       0.016    0.016   0.016   0.016 Task_1.py:6(createDist)

cProfile.run("main(1000000)")
#n = 1000000
#результаты запуска функции при n = 1000000 (n - количество элементов в массиве):
#5598441 function calls in 2.460 seconds
#ncalls tottime percall cumtime percall filename: lineno(function)
#1       0.167    0.167   0.167   0.167 Task_1.py:6(createDist)


#Выводы:
# 1) общее время выполнения программы растет линейно с увеличением количества элементов массива
# линейная сложность O(n)
# 2) время выполнения функции createDist растет линейно с увеличением количества элементов массива O(n)
# линейная сложность O(n)
