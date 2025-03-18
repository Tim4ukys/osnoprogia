# val
# next
class SList:
    pass


# Размер списка
def length(lst):
    r = 0
    while lst is not None:
        r += 1
        lst = lst.next
    return r


# Добавить в голову. Возвращает новое начало списка.
def prepend(lst, data):
    nw = SList()
    nw.next = lst
    nw.val = data
    return nw


# Возвращает значение по его индексу
def get(lst, index):
    for _ in range(index):
        if lst is None:
            break
        lst = lst.next
    return lst.val if lst is not None else None


# Удаляет элемент по его порядковому номеру. Возвращает его данные и новое начало списка.
# Возвращает: [value, list]
def remove(lst, index):
    begin = lst
    for _ in range(index - 1):
        if lst is None:
            return [None, begin]
        lst = lst.next
    if lst is None or lst.next is None:
        return [None, begin]
    elif index == 0:
        return [begin.val , begin.next]

    t = lst.next
    lst.next = t.next
    return [t.val, begin if index == 0 else lst]


# Добавить в хвост. Возвращает новое начало списка.
def append(lst, data):
    begin = lst
    t = SList()
    t.val = data
    t.next = None
    if lst is not None:
        while lst.next is not None:
            lst = lst.next
        lst.next = t
        return begin
    else:
        return t


# Возвращает данные последнего элемента.
def get_last(lst):
    if lst is None:
        return None
    while lst.next is not None:
        lst = lst.next
    return lst.val

# Возвращает первый индекс листа с нужными данными
def find(lst, data):
    return find_custom(lst, lambda v: v == data)


# Удалить первый элемент из списка со значением data. Возвращает новое начало списка.
def remove_first(lst, data):
    if lst is None:
        return None
    elif lst.val == data:
        return lst.next

    begin = lst
    while lst.next is not None:
        prev = lst
        lst = lst.next
        if  lst.val == data:
            prev.next = lst.next
            break

    return begin


# Удалить все элементы из списка со значением data. Возвращает новое начало списка.
def remove_all(lst, data):
    if lst is None:
        return None
    elif lst.val == data:
        lst = lst.next
    begin = lst

    while lst.next is not None:
        prev = lst
        lst = lst.next
        if lst.val == data:
            prev.next = lst.next
            lst = prev

    return begin


#  Скопировать список. Возвращает начало копии.
def copy(lst):
    if lst is None:
        return None
    r = t = SList()
    while True:
        t.val = lst.val
        if lst.next is None:
            t.next = None
            return r

        t.next = SList()
        t = t.next
        lst = lst.next

# Присоединяет в хвост списка lst1 список lst2. Возвращает новое начало объединенного списка.
def concat(lst1, lst2):
    if lst1 is None:
        return lst2
    r = lst1
    while lst1.next is not None:
        lst1 = lst1.next
    lst1.next = lst2
    return r

# Обход списка. Функции func на каждом шаге передаются данные очередного элемента списка.
def foreach(lst, func):
    while lst is not None:
        func(lst.val)
        lst = lst.next


# Возвращает значение и индекс первого элемента, для которого данная функция-предикат возвращает истину.
def find_custom(lst, predicate):
    r = 0
    while lst is not None:
        if predicate(lst.val):
            return r
        lst = lst.next
        r += 1
    return -1
