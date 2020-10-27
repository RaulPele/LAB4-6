"""
Modul care contine functii de sortare a unei liste
"""

from BLL.lists.IO import get_imag, get_real

def imag_desc(a, b):
    """
    Verifica daca a.imag < b.imag
    :param a: numar complex
    :param b: numar complex
    :return True: daca a.imag < b.imag
            False: daca a.imag >=b.imag
    """

    return get_imag(a) < get_imag(b)


def sort_list(myList, condition):
    """
    Sorteaza lista myList dupa o conditie care priveste elementele multimii
    :param myList: lista de numere complexe
    :param condition: conditie dupa care se va sorta lista
    :return sortedList: lista sortata dupa condition
    """

    if len(myList) == 0:
        raise Exception("Lista e goala")

    sortedList = myList.copy()

    for i in range(0, len(sortedList) - 1):
        for j in range(i+1, len(sortedList)):
            if condition(sortedList[i], sortedList[j]):
                aux = sortedList[i]
                sortedList[i] = sortedList[j]
                sortedList[j] = aux

    return sortedList
