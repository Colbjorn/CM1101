import time

def QTE(butn, tim):
    start = time.time()
    hit = input('Hit ' + butn + '! ').lower()
    end = time.time()
    success = False
    if hit == butn and (end-start)<tim:
        success = True
    if success == True:
        print('Success!')
    else:
        print('Fail!')
    return success

QTE('x', 5)