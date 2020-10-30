"""Modul pentru validarea datelor"""


def validate_number(value, type):
    """
    Functia verifica daca valoarea value este de tipul type
    Raise ValueError - daca value nu este de tipul type
    :param value: string reprezentand posibilul numar
    :param type: tip de numere
    :return True: daca numarul din stringul value este de tip type

    """
    if type.__name__ == "int" and not value.isnumeric():
        raise ValueError("Numarul trebuie sa fie de tipul intreg!\n")
    try:
        value = type(value)
    except ValueError:
        raise ValueError("Numarul trebuie sa fie de tipul " + type.__name__ + "!\n")



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