"""
Modul pentru operatii de input/output din lista
"""

import utils.numbers
from data.entities import  Complex

def get_imaginaries(myList, start, end):
    """
    Returneaza o lista continand partile imaginare ale numerelor aflate
    intre start si end
    :param myList: lista de numere complexe
    :param start: pozitia de inceput a secventei
    :param end: pozitia de sfarsit a secventei
    :return imaginaries: lista partilor imaginare dintre start si end
    """

    imaginaries = []
    for i in range(start-1, end):
        c = Complex()
        c.set_imag(myList[i].get_imag())
        imaginaries.append(c)

    return imaginaries


def duplicate(myList, c):
    """
    Returneaza True daca numarul c se afla in lista, False in caz contrar
    :param myList: lista de obiecte Complex
    :param c: obiectul Complex care se cauta in lista
    :return: True- daca c e in lista
            False - daca c nu se afla in lista
    """

    for nr in myList:
        if utils.numbers.isEqual(c, nr):
            return True
    return False


def add_number(myList, c):
    """
    Adauga numarul complex c la finalul listei si returneaza lista obtinuta
    raise Exception - in caz ca numarul exista deja in lista
    :param myList: lista de numere complexe
    :param c: numar complex
    :return newList: lista obtinuta in urma adaugarii
    """

    if duplicate(myList, c):
        raise Exception("Numarul exista deja in lista.")

    newList = copy_list(myList)
    newList.append(c)

    return newList


def insert_number(myList, c, pos):
    """
    Insereaza numarul c pe pozitia pos-1 in myList si returneaza lista obtinuta
    raise Exception - in caz ca numarul exista deja in lista
    :param myList: lista de numere complexe
    :param c: numar complex
    :param pos: pozitie valida din lista
    :return newList: lista obtinuta in urma adaugarii
    """

    if duplicate(myList, c):
        raise Exception("Numarul exista deja in lista.")

    newList = copy_list(myList)
    newList.insert(pos-1, c)

    return newList


def delete_numbers(myList, start, end):
    """
    Elimina elementele din intervalul de pozitii [start, end] si returneaza lista rezultata
    raise Exception - in caz ca lista este goala
    :param myList: lista de numere complexe
    :param start: numar natural reprezentand pozitia de start a secventei
    :param end:  numar natural reprezentand pozitia de sfarsit a secventei
    :return newList: lista obtinuta in urma eliminarii
    """

    if len(myList) == 0:
        raise Exception("Lista este goala")

    newList = copy_list(myList)
    del newList[start-1:end]

    return newList


def format_list(myList):
    """
    Formateaza o lista de obiecte Complex intr-o lista de tipul [a+bj, c+dj...]
    :param myList: lista de numere Complex
    :return listStr: string reprezentand lista
    """
    listStr = "["
    for i in range(0, len(myList) - 1):
        listStr += myList[i].get_complex_string() + ", "

    listStr += myList[len(myList)-1].get_complex_string() + "]"
    return listStr


def copy_list(myList):
    """
    Returneaza o copie a listei myList
    :param myList: lista de obiecte Complex
    :return copy: copia listei myList
    """

    copy=[]
    for c in myList:
        copy.append(c.copy_complex())

    return copy
