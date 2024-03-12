# Case-study #3
# Developers: Ekin Viacheslaw, Amat Tolkochokov, Ilya Sokolov, Askar Gazizov
#
import ru_local as ru

MAX_MONTH = 12


def free_tax():
    '''
    The function determines the annual tax-free amount.
    '''
    amount = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TEXT_FREE_TAX} {ru.NAME[month]} [USD]: '))
        amount += value
    return amount

def revenue():
    '''
    The function determines the annual amount.
    '''
    general_revenue = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TEXT_REVENUE} {ru.NAME[month]} [USD]: '))
        general_revenue += value
    return general_revenue

def main():
    print(ru.CATEGORY)
    category = int(input(ru.MEANING))
    taxable_amount = revenue() - free_tax()

    if category == 1:
    elif category == 2:
    elif category == 3:
    else:
            print(ru.FAIL)


main()