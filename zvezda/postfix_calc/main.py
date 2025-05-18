import postfix_calc
import sys

print('send exit to go exit')
while True:
    s = input('calc: ')
    if s == 'exit':
        sys.exit(0)
    r = None
    try:
        r = postfix_calc.postfix_calc(s)
        print(r)
    except ZeroDivisionError:
        print('division by zero.')
    except ValueError:
        print('invalid symbol.')
    except BufferError:
        print('there are not enough numbers in the expression to calculate.')
    except RuntimeError:
        print('there are non-effective numbers in your expression.')


