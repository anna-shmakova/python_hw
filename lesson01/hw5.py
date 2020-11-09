income = float(input('Укажите сумму выручки: '))
costs = float(input('Укажите сумму издержек: '))
fin_results = income - costs
if fin_results < 0:
    print('Убыток компании составляет: ', -fin_results, 'руб.')
else:
    print('Прибыль компании составила: ', fin_results, 'руб.')
    roi = fin_results / income
    employees = int(input('Укажите количество сотрудников: '))
    profit_emplyee = fin_results / employees
    print('Рентабельность выручки: ', roi, '\nПрибыль на каждого сотрудника: ', profit_emplyee, 'руб.')
