"""
Modul pentru definirea interactiunii dintre utilizator si program
"""
from utils import numbers
import BLL.lists.operations
import BLL.lists.IO
import BLL.lists.sorting
import BLL.lists.filters
from data.validation import validate_number, validate_position, validate_insert_position
from data.entities import Complex

def print_menu(size):
    """
    Afiseaza meniul pentru utilizator
    """
    
    if size != 0:
        print("1. Adaugati un numar complex la finalul listei")
        print("2. Inserati un numar complex pe o pozitie data")
        print("3. Tipariti partea imaginara a numerelor complexe dintr-o secventa")
        print("4. Calculati suma numerelor dintr-o secventa data")
        print("5. Tipariti lista ordonata descrescator dupa partea imaginara")
        print("6. Eliminati toate numerele din lista are au partea reala un numar prim")
        print("7. Eliminati toate numerele din lista care au modulul mai mic, egal sau mai mare\n"
              "decat un numar dat")
        print("8. Stergeti un numar de pe o pozitie data")
        print("9. Stergeti o secventa de numere din lista")
        print("10. Iesire\n")
    else:
        print("1. Adaugati un numar complex la finalul listei")
        print("2. Inserati un numar complex pe o pozitie data")
        print("10. Iesire")


def print_seq_complex(myList, start, end, prop):
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
        listStr = BLL.lists.IO.format_list(myList)
        print(listStr)
        print()


def read_option(size):
    """
    Citeste optiunea utilizatorului si returneaza un raspuns valid
    :return op: optiunea aleasa - str
    """

    if size != 0:
        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    else:
        options = ["1", "2", "10"]

    op = input("Alegeti o optiune: ").strip()

    while op not in options:
        print("Valoare incorecta! Optiunea aleasa trebuie sa fie din multimea", options, '\n')
        op = input("Alegeti o optiune: ").strip()
    return op


def __get_number(type, inputMsg):
    """
    Functia returneaza un numar de tipul type de la tastatura
    :return c: numar de tip type
    """

    while True:
        x = input(inputMsg)
        try:
            validate_number(x, type)
        except ValueError as ex:
            print(str(ex))
        else:
            break

    return type(x)


def get_Complex():
    """
    Returneaza un obiect de tip Complex continand numarul dat de utilizator
    :return number: obiectul Complex format
    """
    print("Numarul complex este de tipul a+bj (a- numar real numit parte reala, b- numar real numit"+
          " coeficient imaginar)\n")
    real = __get_number(float, "Dati partea reala a numarului (a): ")
    imag = __get_number(float, "Dati coeficientul imaginar a numarului (b): ")

    return Complex(real, imag)


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

    x = __get_number(float, "Dati numarul pentru realizarea comparatiei modulelor: ")
    condition = __get_condition(x)

    printMsg = "Lista initiala este: "
    print_seq_complex(myList, 0, len(myList), printMsg)

    filteredList = BLL.lists.filters.filter_elements(myList, condition, x)

    printMsg = "Lista obtinuta in urma eliminarii este: "
    print_seq_complex(filteredList, 0, len(filteredList), printMsg)


def filter_prime(myList):
    """
    Elimina elementele din lista myList care au partea reala un numar prim
    si afiseaza lista obtinuta.
    :param myList: lista de obiecte Complex
    :return myList: lista obtinuta in urma eliminarii
    """

    if len(myList) == 0:
        print("Lista este goala.\n")
        return myList

    condition = "Lista initiala este: "
    print_seq_complex(myList, 0, len(myList), condition)

    filteredList = BLL.lists.filters.filter_elements(myList, numbers.is_prime)

    condition = "Lista obtinuta in urma eliminarii tuturor numerelor cu partea reala prima este: "
    print_seq_complex(filteredList, 0, len(filteredList), condition)


def __get_positions(size):
    """
    Returneaza valorile date de utilizator pentru inceputul si sfarsitul unei secvente
    :param size:
    :return start, end: start- inceputul secventei ; end - sfarsitul secventei
    """

    inputMsg = "Dati pozitia de inceput a secventei: "
    start = __get_position(size, inputMsg)

    inputMsg = "Dati pozitia de sfarsit a secventei: "
    while True:
        end = __get_position(size, inputMsg)
        if start > end:
            print("Pozitia de sfarsit trebuie sa fie mai mare sau egala cu " + str(start) +"\n")
        else:
            break
    return start, end


def sum_secv(myList):
    """
    Preia datele de la utilizator, determina suma si afiseaza rezultatul.
    :param myList: lista de numere complexe
    """

    if len(myList) == 0:
        print("Lista este goala\n")
        return

    start, end = __get_positions(len(myList))
    suma = BLL.lists.operations.det_sum(myList, start, end)
    print_seq_complex(myList, 0, len(myList), "Lista de numere: ")
    print("\nSuma numerelor dintre pozitiile " + str(start) + " si " +str(end) +" este: "+
          suma.get_complex_string() + "\n")


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
    start, end = __get_positions(len(myList))
    imaginaries = BLL.lists.IO.get_imaginaries(myList, start, end)

    printMsg = "Lista originala este:"
    print_seq_complex(myList, 0, len(myList), printMsg)

    printMsg = "Partile imaginare ale numerelor aflate intre pozitiile " + str(start) + " si " + str(end) + " sunt: "
    print_seq_complex(imaginaries, 0, len(imaginaries), printMsg)


def add_number(myList):
    """
    Preia un numar complex de la utilizator, il adauga la finalul listei si afiseaza rezultatul
    returnand lista obtinuta sau afiseaza un mesaj corespunzator daca elementul exista deja
    in lista.
    :param myList: lista de numere complexe
    :return newList: lista obtinuta in urma adaugarii
    """

    c = get_Complex()
    try:
        newList = BLL.lists.IO.add_number(myList, c)
    except Exception as ex:
        print(str(ex))
    else:
        printMsg = "Lista obtinuta in urma adaugarii este: "
        print_seq_complex(newList, 0, len(newList), printMsg)
        return newList

    return myList


def __get_position(size, inputMsg):
    """
    Returneaza o pozitie valida din lista.
    :param size: dimensiunea listei
    :param inputMsg: mesaj referitor la pozitie
    :return pos: pozitia din lista
    """

    while True:
        pos = input(inputMsg)
        try:
            validate_position(pos, size)
        except Exception as ex:
            print(str(ex))
        else:
            break

    return int(pos)


def __get_insert_position(size, inputMsg):
    """
    Returneaza o pozitie valida pentru inserarea unui numar in lista
    :param size: numar natural - dimensiunea listei
    :param inputMsg: mesaj pentru utilizator
    :return pos: pozitie valida pe care se va insera un numar
    """

    while True:
        pos = input(inputMsg)
        try:
            validate_insert_position(pos, size)
        except Exception as ex:
            print(str(ex))
        else:
            break

    return int(pos)


def insert_number(myList):
    """
    Preia un numar complex de la utilizator, il adauga in lista pe o pozitie data si afiseaza rezultatul
    returnand lista obtinuta sau afiseaza un mesaj corespunzator daca elementul exista deja in lista.

    :param myList: lista de numere complexe
    :return newList: lista obtinuta in urma adaugarii
    """

    c = get_Complex()
    pos = __get_insert_position(len(myList), "Dati pozitia pe care va fi inserat numarul " +
                                c.get_complex_string() + ": ")

    try:
        newList = BLL.lists.IO.insert_number(myList, c, pos)
    except Exception as ex:
        print(str(ex))
    else:
        printMsg = "Lista obtinuta in urma inserarii este: "
        print_seq_complex(newList, 0, len(newList), printMsg)
        return newList
    return myList


def delete_number(myList):
    """
    Preia poiztia de la utilizator de pe care se va elimina numarul complex, elimina numarul si afiseaza
    lista rezultata sau un mesaj corespunzator daca lista este goala.
    :param myList: lista de numere complexe
    :return newList: lista rezultata in urma eliminarii
    """

    if len(myList) == 0:
        print("Lista este goala.\n")
        return

    print_seq_complex(myList, 0, len(myList), "Lista initiala este: ")

    pos = __get_position(len(myList), "Dati pozitia din lista de pe care se va elimina numarul complex: ")
    newList = BLL.lists.IO.delete_numbers(myList, pos, pos)

    print_seq_complex(newList, 0, len(newList), "Lista obtinuta in urma eliminarii: ")
    return newList


def delete_sequence(myList):
    """
    Preia pozitiile start, end de la utilizator  si elimina elementele de pe pozitiile [start, end], afiseaza
    rezultatul si returneaza lista obtinuta sau tipareste un mesaj corespunzator daca lista este goala
    :param myList: lista de numere complexe
    :return newList: lista obtinuta in urma eliminarii
    """

    if len(myList) == 0:
        print("Lista este goala.")
        return

    print_seq_complex(myList, 0, len(myList), "Lista initiala este: ")

    start, end = __get_positions(len(myList))
    newList = BLL.lists.IO.delete_numbers(myList, start, end)

    print_seq_complex(newList, 0, len(newList), "Lista rezultata in urma eliminarii este: ")
    return newList


def sort_desc_img(myList):
    """
    Sorteaza si afiseaza lista ordonata descrescator dupa partea imaginara
    :param myList: lista de obiecte Complex
    """
    if len(myList) == 0:
        print("Lista este goala.")

    sortedList = BLL.lists.sorting.sort_list(myList, BLL.lists.sorting.imag_desc)
    print_seq_complex(sortedList, 0, len(sortedList), "Lista sortata descrescator dupa partea imaginara: ")


def run():
    """
    Functia principala care ruleaza programul si apeleaza functiile corespunzatoare optiunilor alese
    de catre utilizator
    """
    myList = []

    noRetFunc = {"3": print_imag_list, "4": sum_secv, "5": sort_desc_img,
                 "6": filter_prime, "7": filter_module}
    func = {"1": add_number, "2": insert_number, "8": delete_number,
            "9": delete_sequence}

    while True:
        print_menu(len(myList))
        op = read_option(len(myList))
        if op == "10":  # iesire din program
            return
        if op in noRetFunc:
            noRetFunc[op](myList)
        else:
            myList= func[op](myList)
        input("Apasati Enter pentru a continua...")

