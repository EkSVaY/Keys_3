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
        if taxable_amount >= 406751:
            tax = (9075 * 0.1 + 27824 * 0.15 + 52449 * 0.25 + 96999 * 0.28 + 218749 * 0.33 +
                   1649 * 0.35 + (taxable_amount - 406751) * 0.396)
        if taxable_amount >= 405101 and taxable_amount <= 406750:
            tax = (9075 * 0.1 + 27824 * 0.15 + 52449 * 0.25 + 96999 * 0.28 +
                   218749 * 0.33 + (taxable_amount - 405101) * 0.35)
        if taxable_amount >= 186351 and taxable_amount <= 405100:
            tax = (9075 * 0.1 + 27824 * 0.15 + 52449 * 0.25 + 96999 * 0.28 +
                   (taxable_amount - 186351) * 0.33)
        if taxable_amount >= 89351 and taxable_amount <= 186350:
            tax = 9075 * 0.1 + 27824 * 0.15 + 52449 * 0.25 + (taxable_amount - 89351) * 0.28
        if taxable_amount >= 36901 and taxable_amount <= 89350:
            tax = 9075 * 0.1 + 27824 * 0.15 + (taxable_amount - 36901) * 0.25
        if taxable_amount >= 9076 and taxable_amount <= 36900:
            tax = 9075 * 0.1 + (taxable_amount - 9076) * 0.15
        if taxable_amount >= 0 and taxable_amount <= 9075:
            tax = taxable_amount * 0.1
        print(tax)
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
                if taxable_amount >= 432201:
            tax = 12950 * 0.1 + 36449 * 0.15 + 78149 * 0.25 + 79049 * 0.28 + \
                  198499 * 0.33 + 27099 * 0.35 + (taxable_amount - 432201) * 0.396
        if taxable_amount >= 405101 and taxable_amount <= 432200:
            tax = 12950 * 0.1 + 36449 * 0.15 + 78149 * 0.25 + 79049 * 0.28 + \
                  198499 * 0.33 + (taxable_amount - 405101) * 0.35
        if taxable_amount >= 206601 and taxable_amount < 405101:
            tax = 12950 * 0.1 + 36449 * 0.15 + 78149 * 0.25 + 79049 * 0.28 + \
                  (taxable_amount - 206601) * 0.33
        if taxable_amount >= 127551 and taxable_amount < 206601:
            tax = 12950 * 0.1 + 36449 * 0.15 + 75049 * 0.25 + (taxable_amount - 127551) * 0.28
        if taxable_amount >= 49401 and taxable_amount < 127551:
            tax = 12950 * 0.1 + 36449 * 0.15 + (taxable_amount - 49401) * 0.25
        if taxable_amount >= 12951 and taxable_amount < 49401:
            tax = 12950 * 0.1 + (taxable_amount - 12951) * 0.15
        if taxable_amount >= 0 and taxable_amount < 12951:
            tax = taxable_amount * 0.1
        print(tax)
    else:
        print(ru.FAIL)


main()
