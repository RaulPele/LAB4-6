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



def validate_position(pos, size):
    """Returneaza true daca pozitia este valida pentru o lista de dimensiune size, altfel False
    :param pos: string reprezentand posibila pozitie
    :param size: numar natural reprezentand dimensiunea listei pentru care se face verificarea
    """
    if (not pos.isnumeric()) or (pos.isnumeric() and (int(pos) < 1 or int(pos)>size)):
        raise Exception("Pozitia trebuie sa fie o valoare naturala intre 1 si " + str(size))


def validate_insert_position(pos, size):
    """
    Returneaza true daca pozitia pos este corecta pentru operatia de inserare a unui numar pe o pozitie din lista
    :param pos: string reprezentand posibila pozitie
    :param size: numar natural reprezentand dimensiunea listei pentru care se face verificarea
    :return True: pozitie valida
            False: pozitie invalida
    """
    if size == 0:
        errorMsg = "Lista este goala. Pozitia de inserare trebuie sa fie egala cu 1"
    else:
        errorMsg = "Pozitia trebuie sa fie o valoare naturala intre 1 si " + str(size+1)

    if not pos.isnumeric():
        raise Exception(errorMsg)
    if (pos.isnumeric()) and (size !=0 and (int(pos) <1 or
                                            int(pos)>size+1) or (size == 0 and int(pos) != 1)):
        raise Exception(errorMsg)

def validate_command(cmd, commands):

    if cmd not in commands:
        raise Exception("Comanda invalida!\n")
    return True