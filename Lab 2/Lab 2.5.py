# 99 bottles of beer.

for bottles in range(99, 0, -1):
    print(str(bottles) + ' bottles of beer on the wall, ' + str(bottles) + ' bottles of beer.')
    print('Take one down, pass it around, ' + str(bottles - 1) + ' bottles of beer on the wall.')