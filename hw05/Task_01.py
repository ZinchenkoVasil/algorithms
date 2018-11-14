import collections
companies = collections.defaultdict(list)
n = int(input("Количество предприятий: "))
s = 0
for i in range(n):
    company_name = input(str(i+1) + "-е предприятие: ")
    for j in range(1,5):
        profit = int(input(f"введите прибыль за {j} квартал: "))
        companies[company_name].append(profit)
        s += profit
    avrg = s / n
print("\nСредняя прибыль: %.0f. Предприятия с годовой прибылью выше среднего:" % avrg)
for company_name in companies:
    if sum(companies[company_name]) > avrg:
        print(company_name)
print("\nСредняя прибыль: %.0f. Предприятия с годовой прибылью ниже среднего:" % avrg)
for company_name in companies:
    if sum(companies[company_name]) < avrg:
        print(company_name)

#print(companies)
