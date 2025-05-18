import postfix_calc

print('send exit to go exit')
def main():
    while True:
        print('calc: ', end='')
        expr = ''
        while True:
            s = input()
            if s == 'exit':
                return
            try:
                expr = expr + ' ' + s
                r = postfix_calc.postfix_calc(expr)
                print(r)
            except ZeroDivisionError:
                print('division by zero.')
            except ValueError:
                print('invalid symbol.')
            except BufferError:
                print('there are not enough numbers in the expression to calculate.')
            except RuntimeError:
                continue
            break


main()
