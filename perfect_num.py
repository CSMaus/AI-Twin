import math
import sys

import numpy as np


def find_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


# now function to find divisor that are not divisible by 2
def find_divisors_not_divisible_by_2(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if i % 2 != 0:
                divisors.append(i)
            if i != n // i and (n // i) % 2 != 0:
                divisors.append(n // i)
    return divisors


# new function find divisor which start from dividing number to 2
# and if divisor is not divisible by 2, then add 1 to it and divide by 2
# and ad it to the list

def find_divisors_divide_to_2(n):
    divisors = []
    simple_num = []

    while True:

        if n % 2 == 0:
            n = n // 2
            divisors.append(n)
        else:
            n = n / 2
            n = round(n)
            simple_num.append(n - 1)
            # divisors.append(n)
        if n == 1:
            divisors.append(1)
            break
    return divisors, simple_num


'''number = 137438691328
# numstr = "191561942608236107294793378084303638130997321548169216"
# numstr = "2658455991569831744654692615953842176"
numstr = "2305843008139952128"
print(len(numstr))
divs = find_divisors(number)
div_no2 = find_divisors_not_divisible_by_2(number)
print(div_no2)
# sum of divisors
print(divs)
print("\nSum of divisors", sum(divs) - number)'''

perfect_num1 = 6
perfect_num2 = 28
perfect_num3 = 496
perfect_num4 = 8128
perfect_num5 = 33550336
perfect_num6 = 8589869056
perfect_num7 = 137438691328
perfect_num8 = 2305843008139952128
perfect_num9 = 2658455991569831744654692615953842176
perfect_num10 = 191561942608236107294793378084303638130997321548169216
perfect_num11 = 13164036458569648337239753460458722910223472318386943117783728128
perfect_num12 = 14474011154664524427946373126085988481573677491474835889066354349131199152128
perfect_num13 = 2356272345726734706578954899670990498847754785839260071014302759750633728317862223970550786
perfect_num14 = 441381112635364226888527867364837927694429383025734013198989569674256504936189812567389134052576
perfect_num15 = 1042731777999398080953233883865090859841788992900187789380027019849183413595961868762139490442368


list_perfect_nums = [perfect_num1, perfect_num2, perfect_num3, perfect_num4, perfect_num5, perfect_num6, perfect_num7,
                     perfect_num8, perfect_num9, perfect_num10, perfect_num11, perfect_num12, perfect_num13,
                     perfect_num14, perfect_num15]

# for num in list_perfect_nums:
#     print(len(str(num)))

divs11, simple_num = find_divisors_divide_to_2(perfect_num11)
print(divs11)
sum_divs = sum(divs11) + sum(simple_num)
print("\nSum of divisors", sum_divs)
print(perfect_num11 == sum_divs)
sys.exit()
# find number calculated by: (2^p -1) * 2^(p-1)
p = 61
num = (2**p - 1) * 2**(p-1)
print(num)
print(len(str(num)))
print(len("2658455991569831744654692615953842176"))

