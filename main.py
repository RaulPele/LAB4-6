
def print_menu(size):
    if size != 0:
        print("1. Tipariti partea imaginara a numerelor complexe dintr-o secventa")
        print("2. Calculati suma numerelor dintr-o secventa data")
        print("4. Iesire\n")


def print_secv(myList, start, end):
    """
    Afiseaza elementele din myList dintre pozitiile start si end

    :param myList: lista de numere compe;xe
    :param start: pozitia de start
    :param end: pozitia finala
    """
    pass


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


def read_option(size):
    # definim optiunile in functie de existenta elementelor in lista
    if(size != 0 ):
        options = ["1", "2", "4"]
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
    noRetFunc = {"1": print_imag_list, "2": sum_secv}
    func = {}
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