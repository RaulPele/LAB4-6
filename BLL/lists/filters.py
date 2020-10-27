"""
Modul pentru functia de filtrare a elementelor dintr-o lista de numere complexe
"""


def filter_elements(myList, condition, *args):
    """
    Elimina elementele din myList care indeplinesc conditia condition
    :param myList: lista de numere complexe
    :param condition: o functie boolean care verifica o conditie
    :return newList: lista rezultata in urma eliminarii
    """

    if len(args) == 0:
        newList = [x for x in myList if not condition(x.real)]
    else:
        newList = [x for x in myList if not condition(args[0], x)]
    return newList
