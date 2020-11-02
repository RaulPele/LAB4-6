"""
Modul pentru definirea interactiunii dintre utilizator si program
"""
from utils import numbers
import BLL.lists.operations
import BLL.lists.IO
import BLL.lists.sorting
import BLL.lists.filters
from data.validation import validate_number, validate_position, validate_insert_position
from data.entities import Complex, ComplexOperations
from ui.menu import  Menu



def create_menus():
    addMenuItems = {"1": "1. Adaugati un numar complex la finalul listei",
                    "2": "2. Inserati un numar complex pe o pozitie data",
                    "3": "3. Inapoi..."}
    addMenuReturnFunctions = {"1": add_number, "2": insert_number}
    addMenuFunctions = {"return": addMenuReturnFunctions, "noreturn": {}}
    addMenu = Menu(addMenuItems, addMenuFunctions)

    modifyMenuItems = {"1": "1. Stergeti un numar de pe o pozitie data",
                       "2": "2. Stergeti o secventa de numere din lista",
                       "3": "3. Inlocuire numar complex din lista",
                       "4": "4. Inapoi..."}
    modifyMenuReturnFunctions = {"1": delete_number, "2": delete_sequence, "3": replace_number}
    modifyMenuFunctions = {"return": modifyMenuReturnFunctions, "noreturn":{}}
    modifyMenu = Menu(modifyMenuItems, modifyMenuFunctions)

    searchMenuItems = {"1": "1. Tipariti partea imaginara a numerelor complexe dintr-o secventa",
                       "2": "2. Tipariti elementele din lista care au modulul mai mic decat 10",
                       "3": "3. Tipariti elementele din lista care au modulul egal cu 10",
                       "4": "4. Inapoi..."}
    searchMenuNoReturnFunctions = {"1": print_imag_list, "2": print_modless10, "3": print_modeq10}
    searchMenuFunctions = {"noreturn": searchMenuNoReturnFunctions, "return":{}}
    searchMenu = Menu(searchMenuItems, searchMenuFunctions)

    operationMenuItems={"1": "1. Calculati suma numerelor dintr-o secventa data",
                        "2": "2. Tipariti lista ordonata descrescator dupa partea imaginara",
                        "3": "3. Determinati produsul numerelor dintr-o secventa",
                        "4": "4. Inapoi..."}
    operationMenuReturnFunctions = {}
    operationMenuNoReturnFunctions = {"1": sum_secv,"2": sort_desc_img, "3": prod_secv}
    operationMenuFunctions = {"return": operationMenuReturnFunctions,
                              "noreturn": operationMenuNoReturnFunctions}
    operationMenu = Menu(operationMenuItems, operationMenuFunctions)

    filterMenuItems = {"1": "1. Eliminati toate numerele din lista are au partea reala un numar prim ",
                       "2": "2. Eliminati toate numerele din lista care au modulul mai mic, egal sau mai mare\n"+
                            "decat un numar dat",
                       "3": "3. Inapoi..."}
    filterMenuNoReturnFunctions = {"1": filter_prime, "2": filter_module}
    filterMenuFunctions = {"noreturn": filterMenuNoReturnFunctions, "return":{}}
    filterMenu = Menu(filterMenuItems, filterMenuFunctions)

    undoMenuItems = {"1": "1. Refaceti ultima operatie din lista. Lista revine la versiunea anterioara",
                     "2": "2. Inapoi..."}
    undoMenuReturnFunctions = {"1": undo_list}
    undoMenuFunctions = {"return": undoMenuReturnFunctions, "noreturn": {}}
    undoMenu = Menu(undoMenuItems, undoMenuFunctions)

    mainMenuItems = {"1": "1. Adaugare numar in lista",
                     "2": "2. Modificare elemente din lista",
                     "3": "3. Cautare numere",
                     "4": "4. Operatii cu elemente din lista",
                     "5": "5. Filtrare",
                     "6": "6. Undo",
                     "7": "7. Iesire"}
    mainMenuSubMenus = {"1": addMenu, "2": modifyMenu, "3": searchMenu,
                        "4": operationMenu, "5": filterMenu, "6": undoMenu}
    mainMenu = Menu(mainMenuItems, None, mainMenuSubMenus)

    Menu.initialize_stack(mainMenu)


def callFunction(complexOp, op):
    currentMenu = Menu.get_currentMenu()

    if Menu.user_exits(op):
        Menu.navigate_backwards()

    menuReturnFunctions = currentMenu.get_menuReturnFunctions()
    menuNoReturnFunctions = currentMenu.get_menuNoReturnFunctions()

    if op in menuReturnFunctions:
        currentMenu.get_functionAt(menuReturnFunctions, op)(complexOp)
    elif op in menuNoReturnFunctions:
        currentMenu.get_functionAt(menuNoReturnFunctions, op)(complexOp)



def get_next_action(complexOp):
    currentMenu = Menu.get_currentMenu()

    op = read_option(len(complexOp.get_complexList()))
    if Menu.user_exits(op):
        Menu.navigate_backwards()
        return

    currentSubMenus = currentMenu.get_subMenus()

    if currentSubMenus is not None:
        if op in currentSubMenus.keys():
            # navigate to submenu
             Menu.navigate_to_submenu(op)
             return
             #display_menu(myList)
        else:
            callFunction(complexOp, op)
    else:
        callFunction(complexOp, op)


def display_menu():
    currentMenu = Menu.get_currentMenu()
    currentMenu.print_menu()
    #return get_next_action(myList)


def read_option(size):
    """
    Citeste optiunea utilizatorului corespunzatoare meniului curent si returneaza un raspuns valid
    :return op: optiunea aleasa - str
    """
    currentMenu = Menu.get_currentMenu()
    options = list(currentMenu.get_menuItems().keys())
    op = input("Alegeti o optiune: ").strip()


    while op not in options:
        print("Valoare incorecta! Optiunea aleasa trebuie sa fie din multimea", options, '\n')
        op = input("Alegeti o optiune: ").strip()
    print()
    return op


def print_seq_complex(myList, start, end, prop):
    """
    Afiseaza elementele din myList dintre pozitiile start si end

    :param myList: lista de numere complexe
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


def get_Complex(inputMsg=None):
    """
    Returneaza un obiect de tip Complex continand numarul dat de utilizator
    :return number: obiectul Complex format
    """
    print("Numarul complex este de tipul a+bj (a- numar real numit parte reala, b- numar real numit"+
          " coeficient imaginar)\n")
    if inputMsg is not None:
        print(inputMsg)

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


def filter_module(complexOp):
    """
    Elimina elementele din myList a caror modul indeplinesc o conditie data
    :param complexOp: obiect de tip ComplexOperation
    :return myList: lista obtinuta in urma eliminarii
    """

    if len(complexOp.get_complexList()) == 0:
        print("Lista este goala.\n")
        return

    x = __get_number(float, "Dati numarul pentru realizarea comparatiei modulelor: ")
    condition = __get_condition(x)

    myList = BLL.lists.IO.copy_list(complexOp.get_complexList())
    printMsg = "Lista initiala este: "
    print_seq_complex(myList, 0, len(myList), printMsg)

    filteredList = BLL.lists.filters.filter_elements(myList, condition, x)

    printMsg = "Lista obtinuta in urma eliminarii este: "
    print_seq_complex(filteredList, 0, len(filteredList), printMsg)


def filter_prime(complexOp):
    """
    Elimina elementele din lista myList care au partea reala un numar prim
    si afiseaza lista obtinuta.
    :param myList: obiect ComplexOperation
    """

    if len(complexOp.get_complexList()) == 0:
        print("Lista este goala.\n")
        return

    myList = BLL.lists.IO.copy_list(complexOp.get_complexList())
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


def sum_secv(complexOp):
    """
    Preia datele de la utilizator, determina suma si afiseaza rezultatul.
    :param myList: lista de numere complexe
    """

    if complexOp.get_complexListSize() == 0:
        print("Lista este goala\n")
        return

    myList = BLL.lists.IO.copy_list(complexOp.get_complexList())
    start, end = __get_positions(len(myList))
    suma = BLL.lists.operations.det_sum(myList, start, end)
    print_seq_complex(myList, 0, len(myList), "Lista de numere: ")
    print("\nSuma numerelor dintre pozitiile " + str(start) + " si " +str(end) +" este: "+
          suma.get_complex_string() + "\n")


def prod_secv(complexOp):
    if complexOp.get_complexListSize() == 0:
        print("Lista este goala\n")
        return

    myList = BLL.lists.IO.copy_list(complexOp.get_complexList())
    start, end = __get_positions(len(myList))
    prod = BLL.lists.operations.det_prod(myList, start, end)
    print_seq_complex(myList, 0, len(myList), "Lista de numere: ")
    print("\nProdusul numerelor dintre pozitiile " + str(start) + " si "+ str(end) + " este: "+
          prod.get_complex_string() +"\n")


def print_imag_list(complexOp):
    """
    Obtine datele de intrare de la utilizator, lista partilor imaginare corespunzatoare
    si apeleaza functia de afisare a partilor imaginare
    a numerelor aflate in myList in interavlul [start, end]
    :param complexOp: obiect ComplexOperation
    """

    if complexOp.get_complexListSize() == 0:
        print("Lista este goala.\n")
        return

    myList = BLL.lists.IO.copy_list(complexOp.get_complexList())
    start, end = __get_positions(len(myList))
    imaginaries = BLL.lists.IO.get_imaginaries(myList, start, end)

    printMsg = "Lista originala este:"
    print_seq_complex(myList, 0, len(myList), printMsg)

    printMsg = "Partile imaginare ale numerelor aflate intre pozitiile " + str(start) + " si " + str(end) + " sunt: "
    print_seq_complex(imaginaries, 0, len(imaginaries), printMsg)


def add_number(complexOp):
    """
    Preia un numar complex de la utilizator, il adauga la finalul listei si afiseaza rezultatul
    returnand lista obtinuta sau afiseaza un mesaj corespunzator daca elementul exista deja
    in lista.
    :param myList: lista de numere complexe
    :return complexOp: obiect de tip complex
    """

    c = get_Complex()
    myList = BLL.lists.IO.copy_list(complexOp.get_complexList())
    try:
        myList = BLL.lists.IO.add_number(myList, c)
    except Exception as ex:
        print(str(ex))
    else:
        printMsg = "Lista obtinuta in urma adaugarii este: "
        print_seq_complex(myList, 0, len(myList), printMsg)
        complexOp.set_complexList(myList)



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


def insert_number(complexOp):
    """
    Preia un numar complex de la utilizator, il adauga in lista pe o pozitie data si afiseaza rezultatul
    returnand lista obtinuta sau afiseaza un mesaj corespunzator daca elementul exista deja in lista.

    :param myList: lista de numere complexe
    :return newList: lista obtinuta in urma adaugarii
    """

    c = get_Complex()
    myList = BLL.lists.IO.copy_list(complexOp.get_complexList())
    pos = __get_insert_position(len(myList), "Dati pozitia pe care va fi inserat numarul " +
                                c.get_complex_string() + ": ")

    try:
        myList = BLL.lists.IO.insert_number(myList, c, pos)
    except Exception as ex:
        print(str(ex))
    else:
        printMsg = "Lista obtinuta in urma inserarii este: "
        print_seq_complex(myList, 0, len(myList), printMsg)
        complexOp.set_complexList(myList)


def delete_number(complexOp):
    """
    Preia poiztia de la utilizator de pe care se va elimina numarul complex, elimina numarul si afiseaza
    lista rezultata sau un mesaj corespunzator daca lista este goala.
    :param myList: lista de numere complexe
    :return newList: lista rezultata in urma eliminarii
    """

    if len(complexOp.get_complexList()) == 0:
        print("Lista este goala.\n")
        return

    myList = BLL.lists.IO.copy_list(complexOp.get_complexList())
    print_seq_complex(myList, 0, len(myList), "Lista initiala este: ")

    pos = __get_position(len(myList), "Dati pozitia din lista de pe care se va elimina numarul complex: ")
    myList = BLL.lists.IO.delete_numbers(myList, pos, pos)

    print_seq_complex(myList, 0, len(myList), "Lista obtinuta in urma eliminarii: ")
    complexOp.set_complexList(myList)


def delete_sequence(complexOp):
    """
    Preia pozitiile start, end de la utilizator  si elimina elementele de pe pozitiile [start, end], afiseaza
    rezultatul si returneaza lista obtinuta sau tipareste un mesaj corespunzator daca lista este goala
    :param myList: lista de numere complexe
    :return newList: lista obtinuta in urma eliminarii
    """

    if len(complexOp.get_complexList()) == 0:
        print("Lista este goala.")
        return

    myList = BLL.lists.IO.copy_list(complexOp.get_complexList())
    print_seq_complex(myList, 0, len(myList), "Lista initiala este: ")

    start, end = __get_positions(len(myList))
    newList = BLL.lists.IO.delete_numbers(myList, start, end)

    print_seq_complex(newList, 0, len(myList), "Lista rezultata in urma eliminarii este: ")
    complexOp.set_complexList(myList)


def sort_desc_img(complexOp):
    """
    Sorteaza si afiseaza lista ordonata descrescator dupa partea imaginara
    :param myList: lista de obiecte Complex
    """
    if len(complexOp.get_complexList()) == 0:
        print("Lista este goala.")
        return

    myList = BLL.lists.IO.copy_list(complexOp.get_complexList())
    myList = BLL.lists.sorting.sort_list(myList, BLL.lists.sorting.imag_desc)
    print_seq_complex(myList, 0, len(myList), "Lista sortata descrescator dupa partea imaginara: ")


def replace_number(complexOp):
    """
    Inlocuieste toate aparitiile unui numar complex din lista cu un numar
    dat de utilizator sau afiseaza un mesaj corespunzator daca numarul
    nu se afla in lista
    :param myList: lista de obiecte Complex
    :return newList: lista obtinuta in urma inlocuirii
    """
    if len(complexOp.get_complexList())==0:
        print("Lista este goala.")
        return

    myList = BLL.lists.IO.copy_list(complexOp.get_complexList())
    print_seq_complex(myList, 0, len(myList), "Lista de numere: ")
    number = get_Complex("Alegeti numarul din lista care va fi inlocuit: ")
    replacement = get_Complex("Alegeti numarul cu care se va inlocui "+number.get_complex_string()+": ")
    try:
        myList = BLL.lists.IO.replace_number(myList, number, replacement)
    except Exception as ex:
        print(str(ex))
    else:
        print_seq_complex(myList, 0, len(myList), "Lista obtinuta in urma inlocuirii: ")
        complexOp.set_complexList(myList)


def print_modless10(complexOp):
    """
    Tipareste numerele din lista care au modulul mai mic decat 10
    :param myList: lista de obiecte Complex
    """
    if len(complexOp.get_complexList()) == 0:
        print("Lista este goala.")
        return
    myList = BLL.lists.IO.copy_list(complexOp.get_complexList())
    print_seq_complex(myList, 0, len(myList), "Lista initiala este: ")
    myList = BLL.lists.filters.filter_elements(myList, numbers.greater_than, 10)
    print_seq_complex(myList, 0, len(myList), "Lista numerelor cu modulul mai mic decat 10: ")


def print_modeq10(complexOp):

    if len(complexOp.get_complexList()) == 0:
        print("Lista este goala")
        return
    myList = BLL.lists.IO.copy_list(complexOp.get_complexList())
    print_seq_complex(myList, 0, len(myList), "Lista initiala este: ")
    myList = BLL.lists.filters.filter_elements(myList,  numbers.less_than, 10)
    myList = BLL.lists.filters.filter_elements(myList, numbers.greater_than, 10)
    print_seq_complex(myList, 0, len(myList), "Lista numerelor cu modulul egal cu 10: ")


def undo_list(complexOp):
    """
    Reface ultima operatie din lista aducand-o la versiunea anterioara.
    :param complexOp: obiect ComplexOperation
    """
    try:
        complexOp.undo()
    except Exception as ex:
        print(str(ex))
    else:
        print_seq_complex(complexOp.get_complexList(), 0, complexOp.get_complexListSize(), "Lista rezultata este: ")


def run():
    """
    Functia principala care ruleaza programul si apeleaza functiile corespunzatoare optiunilor alese
    de catre utilizator
    """

    complexOp = ComplexOperations()
    create_menus()

    while True:

        if Menu.get_stack_size() == 0:
            return

        display_menu()
        get_next_action(complexOp)

