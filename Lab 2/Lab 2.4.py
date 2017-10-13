# 4. Repeatedly read numbers until empty string. Then, print average. Deal w/ no number input.

numlist = []
def func():
    num = input('Input a numbarr.')
    if num == '':
        if len(numlist) != 0:
            print(sum(numlist) / len(numlist))
        else:
            print('No numbers!')
    elif num.isnumeric() == False:
        print('Not numbarr, try again.')
        func()
    else:
        numlist.append(int(num))
        func()

func()