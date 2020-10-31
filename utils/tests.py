"""
Modul de teste
"""
from utils import numbers
import BLL.lists.filters
import BLL.lists.IO
import BLL.lists.sorting
import BLL.lists.operations
import data.validation
from data.entities import Complex


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


def isEqual(list1, list2):
    """Returneaza true daca cele doua liste sunt egale
    :param list1: lista de obiecte Complex
    :param list2: lista de obiecte Complex
    :return True: daca cele doua liste sunt egale"""
    if len(list1) != len(list2):
        return False
    for i in range (0, len(list1)):
        if not numbers.isEqual(list1[i], list2[i]):
            return False
    return True

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
    assert(isEqual(results, correct) == True)

    myList = convert_list([2 + 2j, 3, 2, 7 + 5j])
    results = BLL.lists.filters.filter_elements(myList, numbers.is_prime)
    correct = []
    assert(results == correct)

    myList = convert_list([1, -2 + 2j, 2 + 2j, 6j])
    results = BLL.lists.filters.filter_elements(myList, numbers.less_than, 4)
    correct = convert_list([6j])
    assert(isEqual(results, correct) == True )

    myList = convert_list([1, -2 + 2j, 2 + 2j, 6j])
    results = BLL.lists.filters.filter_elements(myList, numbers.greater_than, 4)
    correct = convert_list([1, -2 + 2j, 2 + 2j])
    assert(isEqual(results, correct) == True )


def test_det_sum():
    result = BLL.lists.operations.det_sum([], 1, 0)
    correct = Complex(0, 0)
    assert(numbers.isEqual(result, correct))

    myList = convert_list([1 + 1j, 2 + 2j, 3, 4j])
    result = BLL.lists.operations.det_sum(myList, 1, 4)
    correct = Complex(6, 7)
    assert(numbers.isEqual(result, correct))

    myList = convert_list([-1, -5 + 3j, 3 - 5j])
    result = BLL.lists.operations.det_sum(myList, 1, 2)
    correct = Complex(-6, 3)
    assert(numbers.isEqual(result, correct))


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

    assert(isEqual(imaginaries, correct))

    myList = convert_list([1j, 2, 4j, -2 - 2j])
    imaginaries = BLL.lists.IO.get_imaginaries(myList, 2, 4)
    correct = convert_list([0j, 4j, -2j])
    imag_convert(correct)
    assert(isEqual(imaginaries, correct))

    myList = convert_list([-2j, -3j, 4j, 5j])
    imaginaries = BLL.lists.IO.get_imaginaries(myList, 1, 4)
    correct = convert_list([-2j, -3j, 4j, 5j])
    imag_convert(correct)
    assert(isEqual(imaginaries, correct))


def test_duplicates():
    c = Complex(2, 2)
    assert (BLL.lists.IO.duplicate([], c) == False)
    myList = convert_list([1, 2 + 2j, 3])
    assert (BLL.lists.IO.duplicate(myList, Complex(0, 4)) == False)
    myList = convert_list([1, 2 + 2j, 3])
    assert(BLL.lists.IO.duplicate(myList, Complex(2, 2)) == True)


def test_add_number():
    myList = convert_list([1j, 2, 4-5j])
    try:
        results = BLL.lists.IO.add_number(myList, Complex(10, 2))
        correct = convert_list([1j, 2, 4-5j, 10+2j])
        assert(isEqual(results, correct) )
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
        assert(isEqual(results, correct))
    except Exception as ex:
        assert(False)

    myList = convert_list([-2, -2j, 3, 4j])
    try:
        results = BLL.lists.IO.insert_number(myList, Complex(0, 2), 2)
        correct = convert_list([-2, 2j, -2j, 3, 4j])
        assert(isEqual(results, correct))
    except Exception as ex:
        assert(False)

    myList = convert_list([-2, -2j, 3, 4j])
    try:
        results = BLL.lists.IO.insert_number(myList, Complex(0, -2), 2)
        assert(False)
    except Exception as ex:
        assert(True)


def test_valid_position():
    assert(data.validation.valid_position("5", 3) == False)
    assert(data.validation.valid_position("5", 10) == True)
    assert(data.validation.valid_position("-5", 10) == False)


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
        assert(isEqual(results, correct))
    except Exception as ex:
        assert(False)


def test_sort_list():
    try:
        myList = convert_list([1, 1 + 2j, 5j, 3j, -100 + 100j])
        results = BLL.lists.sorting.sort_list(myList, BLL.lists.sorting.imag_desc)
        correct = convert_list([-100 + 100j, 5j, 3j, 1+2j, 1])
        assert(isEqual(results, correct))
    except Exception as ex:
        assert(False)

    try:
        sortedList = BLL.lists.sorting.sort_list([], BLL.lists.sorting.imag_desc)
        assert(False)
    except Exception as ex:
        assert(True)


def test_valid_insert_position():
    assert(data.validation.valid_insert_position("5", 3) == False)
    assert(data.validation.valid_insert_position("5", 10) == True)
    assert(data.validation.valid_insert_position("-5", 10) == False)
    assert(data.validation.valid_insert_position("1", 0) == True)
    assert(data.validation.valid_insert_position("10", 9) == True)


def test_validate_number():
    try:
        data.validation.validate_number("123", float)
    except ValueError as ex:
        assert(False)

    try:
        data.validation.validate_number("1a.34", int)
        assert (False)
    except ValueError as ex:
        assert(str(ex) == "Numarul trebuie sa fie de tipul intreg!\n")

    try:
        data.validation.validate_number("12.5", float)
    except ValueError as ex:
        assert(False)

    try:
        data.validation.validate_number("12.5", int)
        assert (False)
    except ValueError as ex:
        assert (str(ex) == "Numarul trebuie sa fie de tipul intreg!\n")

    try:
        data.validation.validate_number("1+2j", complex)
    except ValueError as ex:
        assert (False)

    try:
        data.validation.validate_number("1+aj", complex)
        assert (False)
    except ValueError as ex:
        assert (str(ex) == "Numarul trebuie sa fie de tipul complex!\n")


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

