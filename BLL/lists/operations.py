"""Modul pentru efectuarea unor operatii pe elementele unei liste"""

from data.entities import  Complex

def det_sum(myList, start, end):
    """
    Determina suma elementelor din myList aflate in secventa [start, end]
    :param myList: lista de numere complexe
    :param start: pozitia initiala
    :param end: pozitia finala
    :return suma: suma elementelor din [start, end] (0 - valoare implicita)
    """

    sumaR = 0
    sumaI= 0
    for i in range(start-1, end):
        sumaR += myList[i].get_real()
        sumaI += myList[i].get_imag()
    return Complex(sumaR, sumaI)


def det_prod(myList, start, end):
    """
    Determina produsul elementelor din myList aflate in secventa [start, end]
    :param myList: lista de numere complexe
    :param start: pozitia initiala
    :param end: pozitia finala
    :return suma: produsul elementelor din [start, end] (0 - valoare implicita) (obiect Complex)
    """
    if len(myList) == 0:
        return Complex(0, 0)

    prod = myList[start-1].copy_complex()
    for i in range(start, end):
        prod = Complex.times(prod, myList[i])

    return prod


def isEqual(list1, list2):
    """Returneaza true daca cele doua liste sunt egale
    :param list1: lista de obiecte Complex
    :param list2: lista de obiecte Complex
    :return True: daca cele doua liste sunt egale"""
    if len(list1) != len(list2):
        return False
    for i in range (0, len(list1)):
        if not Complex.isEqual(list1[i], list2[i]):
            return False
    return True
