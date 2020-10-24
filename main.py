# module imports
import ui
import tests

def run():
    """
    Functia principala care ruleaza programul si apeleaza functiile corespunzatoare optiunilor alese
    de catre utilizator
    """
    myList = [2+2j, 2, 3, 7+5j, 4]
    noRetFunc = {"3": ui.print_imag_list,
                 "4": ui.sum_secv, "5": ui.filter_prime, "6": ui.filter_module}
    func = {"1": ui.add_number, "2":ui.insert_number}

    while True:
        ui.print_menu(len(myList))
        op = ui.read_option(len(myList))
        if op == "7":  # iesire din program
            return
        if op in noRetFunc:
            noRetFunc[op](myList)
        else:
            myList = func[op](myList)
        input("Apasati Enter pentru a continua...")


# apel functii
if __name__ == "__main__":
    tests.run_tests()
    run()

