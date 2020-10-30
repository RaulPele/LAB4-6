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
        sumaR +=  myList[i].get_real()
        sumaI += myList[i].get_imag()
    return Complex(sumaR, sumaI)

