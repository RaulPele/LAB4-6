"""
Modul pentru operatii de input/output din lista
"""


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
        imaginaries.append(myList[i].imag)

    return imaginaries


def duplicate(myList, c):
    """
    Returneaza True daca numarul c se afla in lista, False in caz contrar
    :param myList: lista de numere complexe
    :param c: numarul complex care se cauta in lista
    :return: True- daca x e in lista
            False - daca x nu se afla in lista
    """
    if c in myList:
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

    newList = myList.copy()
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
    newList.insert(pos-1, c)

    return newList


def valid_position(pos, size):
    """Returneaza true daca pozitia este valida pentru o lista de dimensiune size, altfel False
    :param pos: string reprezentand posibila pozitie
    :param size: numar natural reprezentand dimensiunea listei pentru care se face verificarea
    """
    if (not pos.isnumeric()) or (pos.isnumeric() and (int(pos) < 1 or int(pos)>size)):
        return False
    return True


#TODO: write test 
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