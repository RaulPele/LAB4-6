"""Modul pentru efectuarea unor operatii pe elementele unei liste"""


def det_sum(myList, start, end):
    """
    Determina suma elementelor din myList aflate in secventa [start, end]
    :param myList: lista de numere complexe
    :param start: pozitia initiala
    :param end: pozitia finala
    :return suma: suma elementelor din [start, end] (0 - valoare implicita)
    """

    suma = 0

    for i in range(start-1, end):
        suma += myList[i]

    return suma
