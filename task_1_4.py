"""
Написать программу «Банковский депозит».
Клиент банка делает депозит на определенный срок.

В зависимости от суммы и срока вклада определяется процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 и более года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 и более года – 6.5 % годовых).
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 и более года — 7.5 % годовых).

Проценты начисляются на депозит в конце каждого месяца.

Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада (в месяцах), а на выходе возвращать сумму вклада на конец срока.
"""


def bank_deposit():
    sum_deposit = int(input('Введите сумму вклада: '))
    term_deposit = int(input('Введите срок вклада (в месяцах): '))

    if sum_deposit <= 10000:
        for i in range(term_deposit):
            if term_deposit <= 6:
                sum_deposit = (sum_deposit * (5 / 12) / 100) + sum_deposit
            elif 6 > term_deposit <= 12:
                sum_deposit = (sum_deposit * (6 / 12) / 100) + sum_deposit
            else:
                sum_deposit = (sum_deposit * (5 / 12) / 100) + sum_deposit

    elif 1000 > sum_deposit <= 100000:
        for i in range(term_deposit):
            if term_deposit <= 6:
                sum_deposit = (sum_deposit * (6 / 12) / 100) + sum_deposit
            elif 6 > term_deposit <= 12:
                sum_deposit = (sum_deposit * (7 / 12) / 100) + sum_deposit
            else:
                sum_deposit = (sum_deposit * (6.5 / 12) / 100) + sum_deposit

    else:
        for i in range(term_deposit):
            if term_deposit <= 6:
                sum_deposit = (sum_deposit * (7 / 12) / 100) + sum_deposit
            elif 6 > term_deposit <= 12:
                sum_deposit = (sum_deposit * (8 / 12) / 100) + sum_deposit
            else:
                sum_deposit = (sum_deposit * (7.5 / 12) / 100) + sum_deposit

    return print(f'Сумма в конце вклада будет: {sum_deposit}')


bank_deposit()
