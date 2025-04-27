import postfix_calc
import test
import sys

print('send exit to go exit')
while True:
    print('calc: ', end='')
    sz = 0
    expr = ''
    while True:
        s = input()
        if s == 'exit':
            sys.exit(0)
        unk = False
        for i in s.split():
            if postfix_calc._isfloat(i):
                sz += 1
            elif i in "+-/*":
                sz -= 1
            else:
                unk = True
                break
        if unk:
            print("Please enter only numbs and +, -, / or *.")
            continue
        expr = expr + " " + s
        if sz <= 1:
            break

    print(postfix_calc.postfix_calc(expr))