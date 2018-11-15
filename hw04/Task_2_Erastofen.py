import cProfile
import timeit

def Erastofen(number=100):
    n = 1000000 # условно берем такую величину начального массива
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

   # вторым элементом является единица, которую не считают простым числом
   # забиваем ее нулем.
    a[1] = 0
    b = []
    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while len(b) < number:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            #добавить простое число в массив простых чисел
            b.append(a[m])
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1
    return b[number - 1]

def main(n = 100):
    return Erastofen(n)

#print(main(100))

timeit.timeit("main()", number=3)
#n = 100
#результаты запуска функции:
#20000000 loops, best of 5: 9.86 nsec per loop
#20000000 loops, best of 5: 9.88 nsec per loop
#50000000 loops, best of 5: 9.89 nsec per loop

cProfile.run("main(100)")
#n = 100
#результаты запуска функции при n = 100:
#646 function calls in 0.351 seconds
#ncalls tottime percall cumtime percall filename: lineno(function)
#1       0.345    0.345   0.345   0.345 Task_2.py:4(Erastofen)

cProfile.run("main(1000)")
#n = 1000
#результаты запуска функции при n = 1000:
#8924 function calls in 0.401 seconds
#ncalls tottime percall cumtime percall filename: lineno(function)
#1       0.394    0.394   0.395   0.395 Task_2.py:4(Erastofen)

cProfile.run("main(10000)")
#n = 10000
#результаты запуска функции при n = 10000:
#114734 function calls in 0.504 seconds
#ncalls tottime percall cumtime percall filename: lineno(function)
#1       0.491    0.491   0.498   0.498 Task_2.py:4(Erastofen)

#Вывод: при увеличении порядка искомого числа время поиска простого числа увеличивается незначительно