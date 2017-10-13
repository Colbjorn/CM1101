# Calculate number of letters/digits in an input string.

inpt = input('Gimme a sentence. GIMME!!1!')
letters = []
digits = []
for i in inpt:
    if i.isdigit():
        digits.append(i)
    elif i.isalpha():
        letters.append(i)
    else:
        pass

print('Letters: ' + str(len(letters)))
print('Digits: ' + str(len(digits)))