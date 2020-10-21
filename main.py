
def print_menu(size):
    """
    Afiseaza meniul pentru utilizator
    """
    if(size !=0 ):
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


def print_imag(myList, start, end):
    """
    Afiseaza partea imaginara a numerelor din intervalul [start, end]
    :param myList: lista de numere complexe
    :param start: pozitia de inceput
    :param end: pozitia de sfarsit
    :return:
    """

    for c in range(start-1, end):
        print("Numarul " + str(myList[c]) +" are partea imaginara "+str(myList[c].imag))
    print()


def print_imag_list(myList):
    """
    Obtine datele de intrare de la utilizator si apeleaza functia de afisare a partilor imaginare
    a unor numere aflate in myList in interavlul [start, end]
    :param myList: lista de numere complexe
    :return:
    """

    if len(myList) == 0:
        print("Lista este goala.\n")
        return
    start, end = get_positions(len(myList))
    print_imag(myList, start, end)


def test_det_sum():
    assert(det_sum([], 1, 0) == 0)
    assert(det_sum([1 + 1j, 2 +2j, 3, 4j], 1, 4) == 6+7j)
    assert(det_sum([-1, -5+3j, 3-5j], 1, 2)==-6+3j)


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


def sum_secv(myList):
    """
    Preia datele de la utilizator, determina suma si afiseaza rezultatul.
    :param myList: lista de numere complexe
    """

    if len(myList) == 0:
        print("Lista este goala\n")
        return

    start, end = get_positions(len(myList))
    suma = det_sum(myList, start, end)
    print(str(myList)+"\nSuma numerelor dintre pozitiile " + str(start) + " si " +str(end) +" este: "+
          str(suma)+"\n")


def test_prime():
    assert (prime(-7) == False)
    assert (prime(0) == False)
    assert (prime(1) == False)
    assert (prime(2) == True)
    assert (prime(11) == True)
    assert (prime(30) == False)

def prime(x):
    """
    Returneaza True daca numarul x este prim, False in caz contrar
    :param x: numar real
    :return True: daca x este prim
    :return False: daca x nu este prim
    """

    if x <= 1:
        return False
    if x % 2 == 0 and x != 2:
        return False

    div = 3
    while div * div <= x:
        if x % div == 0:
            return False
        div += 2
    return True


def test_elim_elements():
    assert(filter_elements([], prime) == [])
    assert(filter_elements([1, -2 + 2j, 2 + 2j, 6j], prime) == [1, -2+2j, 6j])
    assert(filter_elements([2+2j, 3,2, 7+5j], prime) == [])

    assert(filter_elements([1, -2+2j, 2+2j, 6j], less_than, 4) == [6j])
    assert(filter_elements([1, -2+2j, 2+2j, 6j], greater_than, 4) == [1, -2+2j, 2+2j])


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


# test case-urile pentru aceasta functie sunt identice cu cele ale lui filter_elements
def filter_prime(myList):
    """
    Elimina elementele din lista myList si afiseaza lista obtinuta.
    :param myList: lista de numere complexe
    :return myList: lista obtinuta in urma eliminarii
    """

    if(len(myList) == 0):
        print("Lista este goala.\n")
        return myList

    condition = "Lista initiala este: "
    print_secv(myList, 0, len(myList), condition)

    filteredList = filter_elements(myList, prime)

    condition = "Lista obtinuta in urma eliminarii tuturor numerelor cu partea reala prima este: "
    print_secv(filteredList, 0, len(filteredList), condition)


def get_number():
    """
    Functia returneaza numarul cu care se vor compara modulele numerelor din lista.
    :return c: numar real
    """

    x = input("Dati numarul pentru realizarea comparatiei modulelor: ")
    try:
        x = float(x)
    except ValueError:
        print("Numarul introdus trebuie sa fie real\n")
        return get_number()

    return x


def less_than(x, mod):
    return abs(mod) < x


def greater_than(x, mod):
    return x < abs(mod)


def equal_to(x, mod):
    return x == abs(mod)


def get_condition(x):
    """
    Functia returneaza conditia impusa de utilizator cu referire la modulul
    numerelor care se vor elimina.
    :return: condition - conditia < or > or =;
    """

    options = {"<": less_than, ">": greater_than, "=": equal_to}

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

    x = get_number()
    condition = get_condition(x)

    printMsg = "Lista initiala este: "
    print_secv(myList, 0, len(myList), printMsg)

    filteredList = filter_elements(myList, condition, x)

    printMsg = "Lista obtinuta in urma eliminarii este: "
    print_secv(filteredList, 0, len(filteredList), printMsg)


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


def run():
    """
    Functia principala care ruleaza programul si apeleaza functiile corespunzatoare optiunilor alese
    de catre utilizator
    """
    myList = [2+2j, 2, 3, 7+5j, 4]
    noRetFunc = {"1": print_imag_list, "2": sum_secv, "3": filter_prime, "4": filter_module}
    func = {}

    while True:
        print_menu(len(myList))
        op = read_option(len(myList))
        if op == "5":  # iesire din program
            return
        if op in noRetFunc:
            noRetFunc[op](myList)
        else:
            myList = func[op](myList)
        input("Apasati Enter pentru a continua...")


def runTests():
    test_prime()
    test_det_sum()
    test_elim_elements()


#apel functii
runTests()
run()

