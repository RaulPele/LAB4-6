"""
Modul pentru operatii de input/output din lista
"""

import utils.numbers


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
        #imaginaries.append(get_imag(myList[i]))
        pass

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

    newList = myList.copy()
    number = utils.numbers.create_complex(c.real, c.imag)
    newList.insert(pos-1, number)

    return newList


def valid_position(pos, size):
    """Returneaza true daca pozitia este valida pentru o lista de dimensiune size, altfel False
    :param pos: string reprezentand posibila pozitie
    :param size: numar natural reprezentand dimensiunea listei pentru care se face verificarea
    """
    if (not pos.isnumeric()) or (pos.isnumeric() and (int(pos) < 1 or int(pos)>size)):
        return False
    return True


def valid_insert_position(pos, size):
    """
    Returneaza true daca pozitia pos este corecta pentru operatia de inserare a unui numar pe o pozitie din lista
    :param pos: string reprezentand posibila pozitie
    :param size: numar natural reprezentand dimensiunea listei pentru care se face verificarea
    :return True: pozitie valida
            False: pozitie invalida
    """
    if not pos.isnumeric():
        return False
    if (pos.isnumeric()) and (size !=0 and (int(pos) <1 or
                                            int(pos)>size+1) or (size == 0 and int(pos) != 1)):
        return False
    return True


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

    newList = myList.copy()
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
