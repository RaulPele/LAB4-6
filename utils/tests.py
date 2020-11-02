"""
Modul de teste
"""
from utils import numbers
import BLL.lists.filters
import BLL.lists.IO
import BLL.lists.sorting
import BLL.lists.operations
from data.validation import validate_position, validate_number, validate_insert_position
from data.entities import Complex, ComplexOperations


def convert_list(testList):
    """
    Converteste o lista de numere complexe intr-o lista de obiecte Complex
    :param testList: lista de numere complexe
    :return complexList: lista de obiecte Complex
    """
    complexList =[]
    for nr in testList:
        compl = Complex(nr.real, nr.imag)
        complexList.append(compl)
    return complexList


def test_prime():
    assert (numbers.is_prime(-7) == False)
    assert (numbers.is_prime(0) == False)
    assert (numbers.is_prime(1) == False)
    assert (numbers.is_prime(2) == True)
    assert (numbers.is_prime(11) == True)
    assert (numbers.is_prime(30) == False)
    

def test_filter_elements():
    assert(BLL.lists.filters.filter_elements([], numbers.is_prime) == [])

    myList = convert_list([1, -2 + 2j, 2 + 2j, 6j])
    results = BLL.lists.filters.filter_elements(myList, numbers.is_prime)
    correct = convert_list([1, -2 + 2j, 6j])
    assert(BLL.lists.operations.isEqual(results, correct) == True)

    myList = convert_list([2 + 2j, 3, 2, 7 + 5j])
    results = BLL.lists.filters.filter_elements(myList, numbers.is_prime)
    correct = []
    assert(results == correct)

    myList = convert_list([1, -2 + 2j, 2 + 2j, 6j])
    results = BLL.lists.filters.filter_elements(myList, numbers.less_than, 4)
    correct = convert_list([6j])
    assert(BLL.lists.operations.isEqual(results, correct) == True )

    myList = convert_list([1, -2 + 2j, 2 + 2j, 6j])
    results = BLL.lists.filters.filter_elements(myList, numbers.greater_than, 4)
    correct = convert_list([1, -2 + 2j, 2 + 2j])
    assert(BLL.lists.operations.isEqual(results, correct) == True )


def test_det_sum():
    result = BLL.lists.operations.det_sum([], 1, 0)
    correct = Complex(0, 0)
    assert(Complex.isEqual(result, correct))

    myList = convert_list([1 + 1j, 2 + 2j, 3, 4j])
    result = BLL.lists.operations.det_sum(myList, 1, 4)
    correct = Complex(6, 7)
    assert(Complex.isEqual(result, correct))

    myList = convert_list([-1, -5 + 3j, 3 - 5j])
    result = BLL.lists.operations.det_sum(myList, 1, 2)
    correct = Complex(-6, 3)
    assert(Complex.isEqual(result, correct))


def imag_convert(list):
    for i in range(0, len(list)):
        b = Complex()
        b.set_imag(list[i].get_imag())
        list[i] = b


def test_get_imaginaries():
    imaginaries = BLL.lists.IO.get_imaginaries([], 1, 0)
    assert(imaginaries == [])

    myList = convert_list([1, 2, 3])
    imaginaries = BLL.lists.IO.get_imaginaries(myList, 1, 3)
    correct = convert_list([0,  0, 0])
    imag_convert(correct)

    assert(BLL.lists.operations.isEqual(imaginaries, correct))

    myList = convert_list([1j, 2, 4j, -2 - 2j])
    imaginaries = BLL.lists.IO.get_imaginaries(myList, 2, 4)
    correct = convert_list([0j, 4j, -2j])
    imag_convert(correct)
    assert(BLL.lists.operations.isEqual(imaginaries, correct))

    myList = convert_list([-2j, -3j, 4j, 5j])
    imaginaries = BLL.lists.IO.get_imaginaries(myList, 1, 4)
    correct = convert_list([-2j, -3j, 4j, 5j])
    imag_convert(correct)
    assert(BLL.lists.operations.isEqual(imaginaries, correct))


def test_duplicates():
    c = Complex(2, 2)
    assert (BLL.lists.IO.in_list([], c) == False)
    myList = convert_list([1, 2 + 2j, 3])
    assert (BLL.lists.IO.in_list(myList, Complex(0, 4)) == False)
    myList = convert_list([1, 2 + 2j, 3])
    assert(BLL.lists.IO.in_list(myList, Complex(2, 2)) == True)


def test_add_number():
    myList = convert_list([1j, 2, 4-5j])
    try:
        results = BLL.lists.IO.add_number(myList, Complex(10, 2))
        correct = convert_list([1j, 2, 4-5j, 10+2j])
        assert(BLL.lists.operations.isEqual(results, correct) )
    except Exception as ex:
        assert(False)

    try:
        results = BLL.lists.IO.add_number(myList, Complex(4, -5))
        assert(False)
    except Exception as ex:
        assert(True)


def test_insert_number():
    myList = []
    try:
        results = BLL.lists.IO.insert_number(myList, Complex(0, 2), 1)
        correct = convert_list([2j])
        assert(BLL.lists.operations.isEqual(results, correct))
    except Exception as ex:
        assert(False)

    myList = convert_list([-2, -2j, 3, 4j])
    try:
        results = BLL.lists.IO.insert_number(myList, Complex(0, 2), 2)
        correct = convert_list([-2, 2j, -2j, 3, 4j])
        assert(BLL.lists.operations.isEqual(results, correct))
    except Exception as ex:
        assert(False)

    myList = convert_list([-2, -2j, 3, 4j])
    try:
        results = BLL.lists.IO.insert_number(myList, Complex(0, -2), 2)
        assert(False)
    except Exception as ex:
        assert(True)


def test_valid_position():
    try:
        validate_position("5", 3)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "Pozitia trebuie sa fie o valoare naturala intre 1 si 3")

    try:
        validate_position("5", 10)
        assert (True)
    except Exception as ex:
        assert (False)


    try:
        validate_position("-5", 10)
        assert (False)
    except Exception as ex:
        assert (str(ex) == "Pozitia trebuie sa fie o valoare naturala intre 1 si 10")



def test_delete_numbers():
    try:
        newList = BLL.lists.IO.delete_numbers([], 1, 0)
        assert(False)
    except Exception as ex:
        assert(True)

    try:
        myList = convert_list([1, 2j, 3 + 4j, -5j])
        results = BLL.lists.IO.delete_numbers(myList, 1, 3)
        correct = convert_list([-5j])
        assert(BLL.lists.operations.isEqual(results, correct))
    except Exception as ex:
        assert(False)


def test_sort_list():
    try:
        myList = convert_list([1, 1 + 2j, 5j, 3j, -100 + 100j])
        results = BLL.lists.sorting.sort_list(myList, BLL.lists.sorting.imag_desc)
        correct = convert_list([-100 + 100j, 5j, 3j, 1+2j, 1])
        assert(BLL.lists.operations.isEqual(results, correct))
    except Exception as ex:
        assert(False)

    try:
        sortedList = BLL.lists.sorting.sort_list([], BLL.lists.sorting.imag_desc)
        assert(False)
    except Exception as ex:
        assert(True)


def test_valid_insert_position():
    try:
        validate_insert_position("5", 3)
        assert (False)
    except Exception as ex:
        assert (str(ex) == "Pozitia trebuie sa fie o valoare naturala intre 1 si 4")

    try:
        validate_insert_position("5", 10)
        assert (True)
    except Exception as ex:
        assert (False)

    try:
        validate_insert_position("-5", 10)
        assert (False)
    except Exception as ex:
        assert (str(ex) == "Pozitia trebuie sa fie o valoare naturala intre 1 si 11")

    try:
        validate_insert_position("1", 0)
        assert (True)
    except Exception as ex:
        assert (False)

    try:
        validate_insert_position("10", 9)
        assert (True)
    except Exception as ex:
        assert (False)



def test_validate_number():
    try:
        validate_number("123", float)
    except ValueError as ex:
        assert(False)

    try:
        validate_number("1a.34", int)
        assert (False)
    except ValueError as ex:
        assert(str(ex) == "Numarul trebuie sa fie de tipul intreg!\n")

    try:
        validate_number("12.5", float)
    except ValueError as ex:
        assert(False)

    try:
        validate_number("12.5", int)
        assert (False)
    except ValueError as ex:
        assert (str(ex) == "Numarul trebuie sa fie de tipul intreg!\n")

    try:
        validate_number("1+2j", complex)
    except ValueError as ex:
        assert (False)

    try:
        validate_number("1+aj", complex)
        assert (False)
    except ValueError as ex:
        assert (str(ex) == "Numarul trebuie sa fie de tipul complex!\n")


def test_replace_number():
    try:
        number = Complex(1)
        results = BLL.lists.IO.replace_number([], number, Complex(2))
        assert (False)
    except Exception as ex:
        assert (str(ex) == "Numarul " + number.get_complex_string() +" nu se afla in lista!")

    try:
        number = Complex(1, 2)
        myList = convert_list([1+2j, -1-2j, 0, 1+2j, 100+100j])
        results = BLL.lists.IO.replace_number(myList, number, Complex(0, 0))
        correct = convert_list([0, -1-2j, 0, 0, 100+100j])
        assert(BLL.lists.operations.isEqual(results, correct))
    except Exception as ex:
        assert (False)


def test_det_prod():
    myList=[]
    results = BLL.lists.operations.det_prod(myList, 0, 0)
    assert (Complex.isEqual(results, Complex(0, 0)))

    myList = convert_list([1+2j, 3+5j, 20+3j, 3+4j])
    results = BLL.lists.operations.det_prod(myList, 1, 3)
    prod = (1+2j)*(3+5j)*(20+3j)
    correct = Complex(prod.real, prod.imag)
    assert(Complex.isEqual(results, correct))


def test_undo():
    complexOp = ComplexOperations()
    complexOp.set_complexList(convert_list([1+2j]))
    complexOp.set_complexList(convert_list([1+2j, -1+3j]))
    complexOp.set_complexList(convert_list([0, -1+3j]))

    try:
        complexOp.undo()
        assert (BLL.lists.operations.isEqual(complexOp.get_complexList(), convert_list([1+2j, -1+3j])))
    except Exception as ex:
        assert (False)

    try:
        complexOp.undo()
        assert (BLL.lists.operations.isEqual(complexOp.get_complexList(), convert_list([1+2j])))
    except Exception as ex:
        assert (False)

    try:
        complexOp.undo()
        assert (BLL.lists.operations.isEqual(complexOp.get_complexList(), []))
    except Exception as ex:
        assert (False)

    try:
        complexOp.undo()
        assert (False)
    except Exception as ex:
        assert (str(ex)=="Asupra listei nu s-au efectuat operatii de modificare.\n")


def run_tests():
    test_prime()
    test_filter_elements()
    test_det_sum()
    test_get_imaginaries()
    test_duplicates()
    test_add_number()
    test_insert_number()
    test_valid_position()
    test_valid_insert_position()
    test_delete_numbers()
    test_sort_list()
    test_validate_number()
    test_replace_number()
    test_det_prod()
    test_undo()