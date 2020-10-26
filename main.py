# module imports
import ui
import tests

def run():
    """
    Functia principala care ruleaza programul si apeleaza functiile corespunzatoare optiunilor alese
    de catre utilizator
    """
    myList = []
    noRetFunc = {"3": ui.print_imag_list, "4": ui.sum_secv, "5": ui.sort_desc_img,
                 "6": ui.filter_prime, "7": ui.filter_module}
    func = {"1": ui.add_number, "2": ui.insert_number, "8": ui.delete_number,
            "9": ui.delete_sequence}

    while True:
        ui.print_menu(len(myList))
        op = ui.read_option(len(myList))
        if op == "10":  # iesire din program
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

