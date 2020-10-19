
def print_menu(size):
    if size != 0:
        print("1. Tipariti partea imaginara a numerelor complexe dintr-o secventa")
        print("2. Calculati suma numerelor dintr-o secventa data")
        print("3. Eliminati toate numerele din lista are au partea reala un numar prim")
        print("4. Iesire\n")


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
    for c in range(start-1, end):
        print("Numarul " + str(myList[c]) +" are partea imaginara "+str(myList[c].imag))
    print()


def print_imag_list(myList):
    start, end = get_positions(len(myList))
    print_imag(myList, start, end)


def det_sum(myList, start, end):
    suma = 0

    for i in range(start-1, end):
        suma += myList[i]

    return suma


def sum_secv(myList):
    start, end = get_positions(len(myList))
    suma = det_sum(myList, start, end)
    print(str(myList)+"\nSuma numerelor dintre pozitiile " + str(start) + " si " +str(end) +" este: "+
          str(suma)+"\n")


def prime(x):
    if x < 1:
        return False
    if x % 2 == 0 and x !=2:
        return False

    div = 3
    while div * div <= x:
        if x % div == 0:
            return False
        div += 2
    return True


def elim_elements(myList, condition):
    newList = list.copy(myList)

    for c in newList:
        if condition(c.real):
            newList.remove(c)


    return newList

def elim_prime(myList):
    condition = "Lista initiala este: "
    print_secv(myList, 0, len(myList), condition)

    myList = elim_elements(myList, prime)

    condition = "Lista obtinuta in urma eliminarii tuturor numerelor cu partea reala prima este: "
    print_secv(myList, 0, len(myList), condition)

    return myList

def read_option(size):
    # definim optiunile in functie de existenta elementelor in lista
    if(size != 0 ):
        options = ["1", "2", "3", "4"]
    else: options = []

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
    myList = [1+2j, -2+10j, 13-14j, 10, 5j]
    #myList = []
    noRetFunc = {"1": print_imag_list, "2": sum_secv}
    func = {"3": elim_prime}

    while True:
        print_menu(len(myList))
        op = read_option(len(myList))
        if op == "4":  # iesire din program
            return
        if(op in noRetFunc):
            noRetFunc[op](myList)
        else:
            myList = func[op](myList)


#apel functii
run()