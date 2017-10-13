# Lab 1 too basic for notes.

# 1. Odd or even?
numb3r = int(input('Numb3r pl0x '))
if abs(numb3r)%2 == 0:
    print('Numb3r evn')
else:
    print('Numb3r od')

# 2. Input height(cm) + mass (kg), output circumference(inches eugh).
# Volume of cylinder person V = pi*(r**2)*h.
# Circumference C = 2*pi*r.
# Density rho=m/V.
# Humans barely float in water, thus rho(human) == rho(water).

height = int(input('How talls u hev in centermeters '))
mass = int(input('How fat ar u in kegs '))
# Density of water == 1g/cm**3 == 0.001 kg/cm**3
# Volume = m/density
volume = mass / 0.001
import math
radius = math.sqrt(volume/(height*math.pi))
circumference_cm = 2*math.pi*radius
circumference_inches = circumference_cm/2.54
print('Your cilyndrical circumference is ' + str(circumference_inches) + ' in barbaric imperial inch units, you archaic traceback error of a human.')

# 3. Print largest of 3 numbers using only if statements.
num1 = int(input('Num1 pl0x'))
num2 = int(input('Num2 pls'))
num3 = int(input('Num3, for the love of god, num3 I beg you'))
if num1>num2:
    if num1>num3:
        print(str(num1) + ' is bgr')
    elif num1 == num3:
        print('Tried to be cheeky eh? Both ' + str(num1) + ' and ' + str(num3) + ' are the biggest.')
    else:
        print(str(num3) + ' is begro')
elif num2>num1:
    if num2>num3:
        print(str(num2) + ' is beggar')
    elif num2 == num3:
        print('Both ' + str(num2) + ' and ' + str(num3) + ' are biggest ye cheeky bugger.')
    else:
        print(str(num3) + ' is borg')
elif num1 == num2:
    if num1 > num3:
        print('Both ' + str(num1) + ' and ' + str(num2) + ' are biggest smartass.')
    else:
        print(str(num3) + ' bg.')
else:
    print(str(num3) + ' is the biggest number.')

