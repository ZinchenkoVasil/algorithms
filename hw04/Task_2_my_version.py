import cProfile
import timeit

def SearchSimple(number=100):
    i = 1 # счетчик номера простого числа
    if number <= 1:
        return 2
    n = 3
    while True:
        # проверка на простоту числа
        if IsSimple(n):
            i += 1
            if i == number:
                return n
        n += 1


def IsSimple(n):
    limit = n // 2 + 1
    res = True
    for i in range(2, limit):
        if n % i == 0:
            res = False
    return res

def main(n = 100):
    return SearchSimple(n)

#print(main(100))

timeit.timeit("main()", number=3)
#n = 100
#результаты запуска функции:
#50000000 loops, best of 5: 9.84 nsec per loop
#50000000 loops, best of 5: 9.87 nsec per loop
#20000000 loops, best of 5: 9.84 nsec per loop

cProfile.run("main(100)")
#n = 100
#результаты запуска функции при n = 100:
#544 function calls in 0.005 seconds
#ncalls tottime percall cumtime percall filename: lineno(function)
#539    0.005    0.000    0.005   0.000 Task_2_my_version.py:18(IsSimple)
#1      0.000    0.000    0.005   0.005 Task_2_my_version.py:4(SearchSimple)

cProfile.run("main(1000)")
#n = 1000
#результаты запуска функции при n = 1000:
#7922 function calls in 1.263 seconds
#ncalls tottime percall cumtime percall filename: lineno(function)
#7917    1.261    0.000  1.261    0.000 Task_2_my_version.py:18(IsSimple)
#1       0.002    0.002  1.263    1.263 Task_2_my_version.py:4(SearchSimple)

#cProfile.run("main(10000)")
#n = 10000
#результаты запуска функции при n = 10000:
#104732 function calls in 384.880 seconds
#ncalls tottime percall cumtime percall filename: lineno(function)
#104727 384.798  0.004  384.798   0.004 Task_2_my_version.py:18(IsSimple)
#1      0.082    0.082  384.880 384.880 Task_2_my_version.py:4(SearchSimple)


#Вывод: при увеличении порядка искомого числа время поиска простого числа резко увеличивается.
#Чтобы найти 10000-е простое число, пришлось ждать больше 6 минут (385 секунд).
#Время реализации моего алгоритма растет по экспоненте. Если сравнить с алгоритмом Эратосфена, то мой алгоритм на малых значния (n < 100) работает быстрее.
# Но уже при n = 1000 моя реализация поиска простых чисел показывает намного худший результат.