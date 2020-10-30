"""
Modul care contine functii de sortare a unei liste
"""

from BLL.lists.IO import copy_list


def imag_desc(a, b):
    """
    Verifica daca partea imaginara a lui a este mai mica decat a lui b
    :param a: obiect Complex
    :param b: obiect Complex
    :return True: daca a.get_imag() < b.get_imag()
            False: daca a.get_imag() >=b.get_imag()
    """

    return a.get_imag() < b.get_imag()


def sort_list(myList, condition):
    """
    Sorteaza lista myList dupa o conditie care priveste elementele multimii
    :param myList: lista de obiecte Complex
    :param condition: conditie dupa care se va sorta lista
    :return sortedList: lista sortata dupa condition
    """

    if len(myList) == 0:
        raise Exception("Lista e goala")

    sortedList = copy_list(myList)

    for i in range(0, len(sortedList) - 1):
        for j in range(i+1, len(sortedList)):
            if condition(sortedList[i], sortedList[j]):
                aux = sortedList[i]
                sortedList[i] = sortedList[j]
                sortedList[j] = aux

    return sortedList
