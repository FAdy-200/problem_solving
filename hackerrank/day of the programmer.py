def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 100 == 0 and year % 400 == 0:
        leap = True
    return leap


year = int(input())
x = is_leap(year)
if year == 1918:
    print('26.09.1918')
elif year > 1918:
    if x:
        print('12.09.{}'.format(year))
    else:
        print('13.09.{}'.format(year))
else:
    if x:
        print('13.09.{}'.format(year))
    else:
        print('12.09.{}'.format(year))








































































































