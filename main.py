# module imports
import ui


def run():
    """
    Functia principala care ruleaza programul si apeleaza functiile corespunzatoare optiunilor alese
    de catre utilizator
    """
    myList = [2+2j, 2, 3, 7+5j, 4]
    noRetFunc = {"1": ui.print_imag_list, "2": ui.sum_secv, "3": ui.filter_prime, "4": ui.filter_module}
    func = {}

    while True:
        ui.print_menu(len(myList))
        op = ui.read_option(len(myList))
        if op == "5":  # iesire din program
            return
        if op in noRetFunc:
            noRetFunc[op](myList)
        else:
            myList = func[op](myList)
        input("Apasati Enter pentru a continua...")

"""
def runTests():
    test_prime()
    test_det_sum()
    test_elim_elements()
"""

# apel functii
#runTests()
run()

