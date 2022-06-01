"""
Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная
ежемесячная сумма пополнения вклада. Считаем, что клиент вносит средства в последний день каждого месяца, кроме первого
и последнего. Если 3м аргументом передан 0, то вызов должен быть совпадать с задачей 4.
"""
# Идея следующая, при вносимой суммы равной 0 идем в файл task_1_4 и выполняем функцию в нем, при сумме больше 0, выполняем
# bank_deposit_new добавляя к сумме депозита ежемесячную сумму. (надо только все проверить:))

cash_in = int(input('Введите ежемесячную сумму пополнения вклада: '))


def bank_deposit_new():
    sum_deposit = int(input('Введите сумму вклада: '))
    term_deposit = int(input('Введите срок вклада (в месяцах): '))

    if sum_deposit <= 10000:
        for i in range(term_deposit):
            if term_deposit <= 6:
                sum_deposit = (sum_deposit * (5 / 12) / 100) + sum_deposit + cash_in
            elif 6 > term_deposit <= 12:
                sum_deposit = (sum_deposit * (6 / 12) / 100) + sum_deposit + cash_in
            else:
                sum_deposit = (sum_deposit * (5 / 12) / 100) + sum_deposit + cash_in

    elif 1000 > sum_deposit <= 100000:
        for i in range(term_deposit):
            if term_deposit <= 6:
                sum_deposit = (sum_deposit * (6 / 12) / 100) + sum_deposit + cash_in
            elif 6 > term_deposit <= 12:
                sum_deposit = (sum_deposit * (7 / 12) / 100) + sum_deposit + cash_in
            else:
                sum_deposit = (sum_deposit * (6.5 / 12) / 100) + sum_deposit + cash_in
    else:
        for i in range(term_deposit):
            if term_deposit <= 6:
                sum_deposit = (sum_deposit * (7 / 12) / 100) + sum_deposit + cash_in
            elif 6 > term_deposit <= 12:
                sum_deposit = (sum_deposit * (8 / 12) / 100) + sum_deposit + cash_in
            else:
                sum_deposit = (sum_deposit * (7.5 / 12) / 100) + sum_deposit + cash_in

    return print(f'Сумма в конце вклада будет: {sum_deposit}')


if cash_in == 0:
    from task_1_4 import bank_deposit
    bank_deposit()
else:
    bank_deposit_new()
