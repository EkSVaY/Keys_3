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
    rev = revenue()
    print(ru.YEAR_SAL, rev)
    free = free_tax()
    print(ru.FREE_SUM, free)
    taxable_amount = rev - free

    if category == 1:
        print("aex")
    elif category == 2:
            if taxable_amount > 457601:
                tax = 18151 * 0.1 + 55649 * 0.15 + 75049 * 0.25 + 77999 * 0.28 + \
                      (405100 - 226851) * 0.33 + (457600 - 405101) * 0.35 + \
                      (taxable_amount - 457601) * 0.396
            if taxable_amount > 405101 and taxable_amount <= 457601:
                tax = 18150 * 0.1 + 55649 * 0.15 + 75049 * 0.25 + 77999 * 0.28 + \
                      (405100 - 226851) * 0.33 + (taxable_amount - 405101) * 0.35
            if taxable_amount > 226851 and taxable_amount <= 405101:
                tax = 18150 * 0.1 + 55649 * 0.15 + 75049 * 0.25 + 77999 * 0.28 + \
                      (taxable_amount - 226851) * 0.33
            if taxable_amount > 148851 and taxable_amount <= 226851:
                tax = 18150 * 0.1 + 55649 * 0.15 + 75049 * 0.25 + (taxable_amount - 148851) * 0.28
            if taxable_amount > 73801 and taxable_amount <= 148851:
                tax = 18150 * 0.1 + 55649 * 0.15 + (taxable_amount - 73801) * 0.25
            if taxable_amount > 18151 and taxable_amount <= 73801:
                tax = 18150 * 0.1 + (taxable_amount - 18151) * 0.15
            if taxable_amount >= 0 and taxable_amount <= 18151:
                tax = taxable_amount * 0.1
            print(tax)

    elif category == 3:
        print("")
    else:
        print(ru.FAIL)


main()