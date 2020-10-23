"""
Modul pentru operatii de input/output din lista
"""

#TODO: write test function


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

