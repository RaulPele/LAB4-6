"""
Modul pentru definirea interactiunii dintre utilizator si program
"""
import numbers
import lists.filters
import lists.operations
import lists.IO


def print_menu(size):
    """
    Afiseaza meniul pentru utilizator
    """
    
    if size != 0:
        print("1. Tipariti partea imaginara a numerelor complexe dintr-o secventa")
        print("2. Calculati suma numerelor dintr-o secventa data")
        print("3. Eliminati toate numerele din lista are au partea reala un numar prim")
        print("4. Eliminati toate numerele din lista care au modulul mai mic, egal sau mai mare\n"
              "decat un numar dat")
        print("5. Iesire\n")
    else:
        print("5. Iesire")


def print_secv(myList, start, end, prop):
    """
    Afiseaza elementele din myList dintre pozitiile start si end

    :param myList: lista de numere compe;xe
    :param start: pozitia de start
    :param end: pozitia finala
    :param prop: proprietatea in urma careia s-a ajuns la aceasta secventa (None implicit)
    """
    
    if len(myList) == 0:
        print("Lista este goala.\n")
    else:
        if prop != None:
            print(prop)
        print(myList)
        print()


def read_option(size):
    """
    Citeste optiunea utilizatorului si returneaza un raspuns valid
    :return op: optiunea aleasa - str
    """

    if size != 0:
        options = ["1", "2", "3", "4", "5"]
    else:
        options = ["5"]

    op = input("Alegeti o optiune: ").strip()

    while op not in options:
        print("Valoare incorecta! Optiunea aleasa trebuie sa fie din multimea", options, '\n')
        op = input("Alegeti o optiune: ").strip()
    return op


def __get_number():
    """
    Functia returneaza numarul cu care se vor compara modulele numerelor din lista.
    :return c: numar real
    """

    x = input("Dati numarul pentru realizarea comparatiei modulelor: ")
    try:
        x = float(x)
    except ValueError:
        print("Numarul introdus trebuie sa fie real\n")
        return __get_number()

    return x


def __get_condition(x):
    """
    Functia returneaza conditia impusa de utilizator cu referire la modulul
    numerelor care se vor elimina.
    :return: condition - conditia < or > or =;
    """

    options = {"<": numbers.less_than, ">": numbers.greater_than, "=": numbers.equal_to}

    comp = input("Modulele numerelor care vor fi eliminate sunt mai mici(<), mai mari(>) sau egale(=)\n"
                 "decat  numarul "+str(x)+ "?\n")

    while comp not in options:
        print("Raspuns invalid. Raspunsul dat trebuie sa fie din multimea", options.keys())
        comp = input("Modulele numerelor care vor fi eliminate sunt mai mici(<), mai mari(>) sau egale(=)\n"
                     "numarul " + str(x) + "?\n")

    return options[comp]


def filter_module(myList):
    """
    Elimina elementele din myList a caror modul indeplinesc o conditie data
    :param myList: lista de numere complexe
    :return myList: lista obtinuta in urma eliminarii
    """

    if len(myList) == 0:
        print("Lista este goala.\n")
        return myList

    x = __get_number()
    condition = __get_condition(x)

    printMsg = "Lista initiala este: "
    print_secv(myList, 0, len(myList), printMsg)

    filteredList = lists.filters.filter_elements(myList, condition, x)

    printMsg = "Lista obtinuta in urma eliminarii este: "
    print_secv(filteredList, 0, len(filteredList), printMsg)


def filter_prime(myList):
    """
    Elimina elementele din lista myList si afiseaza lista obtinuta.
    :param myList: lista de numere complexe
    :return myList: lista obtinuta in urma eliminarii
    """

    if len(myList) == 0:
        print("Lista este goala.\n")
        return myList

    condition = "Lista initiala este: "
    print_secv(myList, 0, len(myList), condition)

    filteredList = lists.filters.filter_elements(myList, numbers.is_prime)

    condition = "Lista obtinuta in urma eliminarii tuturor numerelor cu partea reala prima este: "
    print_secv(filteredList, 0, len(filteredList), condition)


def get_positions(size):
    """
    Returneaza valorile date de utilizator pentru inceputul si sfarsitul unei secvente
    :param size:
    :return start, end: start- inceputul secventei ; end - sfarsitul secventei
    """

    start = input("Dati pozitia de inceput a secventei: ")
    while (not start.isnumeric()) or (start.isnumeric() and (int(start) < 1 or int(start)>size)):
        print("Pozitia de inceput trebuie sa fie o valoare intre 1 si " + str(size) + ".")
        start = input("Dati pozitia de inceput a secventei: ")

    start = int(start)

    end = input("Dati pozitia de sfarsit a secventei: ")
    while (not end.isnumeric()) or (end.isnumeric() and (int(end) < 1 or int(end)>size or int(end)<start)):
        print("Pozitia de sfarsit trebuie sa fie o valoare intre 1 si "+ str(size) + " mai mica"+
              " ca pozitia de inceput.")
        end = input("Dati pozitia de sfarsit a secventei: ")

    end = int(end)
    return start, end


def sum_secv(myList):
    """
    Preia datele de la utilizator, determina suma si afiseaza rezultatul.
    :param myList: lista de numere complexe
    """

    if len(myList) == 0:
        print("Lista este goala\n")
        return

    start, end = get_positions(len(myList))
    suma = lists.operations.det_sum(myList, start, end)
    print(str(myList)+"\nSuma numerelor dintre pozitiile " + str(start) + " si " +str(end) +" este: "+
          str(suma)+"\n")


def print_imag_list(myList):
    """
    Obtine datele de intrare de la utilizator, lista partilor imaginare corespunzatoare
    si apeleaza functia de afisare a partilor imaginare
    a numerelor aflate in myList in interavlul [start, end]
    :param myList: lista de numere complexe
    """

    if len(myList) == 0:
        print("Lista este goala.\n")
        return
    start, end = get_positions(len(myList))
    imaginaries = lists.IO.get_imaginaries(myList, start, end)

    printMsg = "Lista originala este:"
    print_secv(myList, 0, len(myList), printMsg)

    printMsg = "Partile imaginare ale numerelor aflate intre pozitiile " + str(start) + " si " + str(end) + " sunt: "
    print_secv(imaginaries, 0, len(imaginaries), printMsg)

