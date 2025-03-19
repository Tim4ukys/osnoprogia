# val
# next
class SList:
    pass


# Размер списка
def length(lst):
    l = lst
    r = 0
    while l:
        r += 1
        l = l.next
    return r


# Добавить в голову. Возвращает новое начало списка.
def prepend(lst, data):
    nw = SList()
    nw.next = lst
    nw.val = data
    return nw


# Возвращает значение по его индексу
def get(lst, index):
    l = lst
    for _ in range(index):
        if not l:
            break
        l = l.next
    return l.val if l else None


# Удаляет элемент по его порядковому номеру. Возвращает его данные и новое начало списка.
# Возвращает: value, list
def remove(lst, index):
    begin = l = lst
    for _ in range(index - 1):
        if not l:
            return None, begin
        l = l.next
    if not l or not l.next:
        return None, begin
    elif index == 0:
        return begin.val, begin.next

    t = l.next
    l.next = t.next
    return (t.val, begin) if index == 0 else l


# Добавить в хвост. Возвращает новое начало списка.
def append(lst, data):
    begin = lst
    t = SList()
    t.val = data
    t.next = None
    if lst:
        l = lst
        while l.next:
            l = l.next
        l.next = t
        return begin
    else:
        return t


# Возвращает данные последнего элемента.
def get_last(lst):
    if not lst:
        return None
    l = lst
    while l.next:
        l = l.next
    return l.val

# Возвращает первый индекс листа с нужными данными
def find(lst, data):
    return find_custom(lst, lambda v: v == data)[1]


# Удалить первый элемент из списка со значением data. Возвращает новое начало списка.
def remove_first(lst, data):
    if not lst:
        return None
    elif lst.val == data:
        return lst.next

    begin = lst
    l = lst
    while l.next:
        prev = l
        l = l.next
        if  l.val == data:
            prev.next = l.next
            break

    return begin


# Удалить все элементы из списка со значением data. Возвращает новое начало списка.
def remove_all(lst, data):
    l = lst
    if not lst:
        return None
    elif l.val == data:
        l = l.next
    begin = l

    while l.next:
        prev = l
        l = l.next
        if l.val == data:
            prev.next = l.next
            l = prev

    return begin


#  Скопировать список. Возвращает начало копии.
def copy(lst):
    if not lst:
        return None
    r = t = SList()
    l = lst
    while True:
        t.val = l.val
        if not l.next:
            t.next = None
            return r

        t.next = SList()
        t = t.next
        l = l.next

# Присоединяет в хвост списка lst1 список lst2. Возвращает новое начало объединенного списка.
def concat(lst1, lst2):
    if not lst1:
        return lst2
    l = lst1
    while l.next:
        l = l.next
    l.next = lst2
    return lst1

# Обход списка. Функции func на каждом шаге передаются данные очередного элемента списка.
def foreach(lst, func):
    l = lst
    while l:
        func(l.val)
        l = l.next


# Возвращает значение и индекс первого элемента, для которого данная функция-предикат возвращает истину.
def find_custom(lst, predicate):
    r = 0
    l = lst
    while l:
        if predicate(l.val):
            return l.val, r
        l = l.next
        r += 1
    return None, -1
