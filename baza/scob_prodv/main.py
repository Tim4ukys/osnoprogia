def check_brackets(expression):
    stack = list()

    brck = {"}":  "{", "]": "[", ')': '(', '>': '<'}

    for i in expression:
        if i in brck.values():
            stack.append(i)
        elif i in brck.keys() and stack.pop() != brck[i]:
            return 0
    return 1


assert(check_brackets("{()[()]}<<<>>>") == 1)
assert(check_brackets("{()[(123)1234]314}1324<1234<<>>413>1324") == 1)
assert(check_brackets("{}()<({}<>)>") == 1)
assert(check_brackets("[(])") == 0)
assert(check_brackets("{{[]]}}") == 0)