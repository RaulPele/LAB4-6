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
