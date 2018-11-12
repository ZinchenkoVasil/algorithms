companies = {}
n = int(input("Количество предприятий: "))
s = 0
for i in range(n):
    company_name = input(str(i+1) + "-е предприятие: ")
    profit = [0, 0, 0, 0]
    profit[0] = int(input("введите прибыль за 1 квартал: "))
    profit[1] = int(input("введите прибыль за 2 квартал: "))
    profit[2] = int(input("введите прибыль за 3 квартал: "))
    profit[3] = int(input("введите прибыль за 4 квартал: "))
    companies[company_name] = profit
    s += sum(profit)
    avrg = s / n
print("\nСредняя прибыль: %.0f. Предприятия с годовой прибылью выше среднего:" % avrg)
for company_name in companies:
    if sum(companies[company_name]) > avrg:
        print(company_name)
print("\nСредняя прибыль: %.0f. Предприятия с годовой прибылью ниже среднего:" % avrg)
for company_name in companies:
    if sum(companies[company_name]) < avrg:
        print(company_name)

