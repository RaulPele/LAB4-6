"""
Modul de teste
"""
from utils import numbers
import BLL.lists.filters
import BLL.lists.IO
import BLL.lists.sorting
import BLL.lists.operations
import data.validation

def test_prime():
    assert (numbers.is_prime(-7) == False)
    assert (numbers.is_prime(0) == False)
    assert (numbers.is_prime(1) == False)
    assert (numbers.is_prime(2) == True)
    assert (numbers.is_prime(11) == True)
    assert (numbers.is_prime(30) == False)
    

def test_filter_elements():
    assert(BLL.lists.filters.filter_elements([], numbers.is_prime) == [])
    assert(BLL.lists.filters.filter_elements([1, -2 + 2j, 2 + 2j, 6j], numbers.is_prime) == [1, -2 + 2j, 6j])
    assert(BLL.lists.filters.filter_elements([2 + 2j, 3, 2, 7 + 5j], numbers.is_prime) == [])

    assert(BLL.lists.filters.filter_elements([1, -2 + 2j, 2 + 2j, 6j], numbers.less_than, 4) == [6j])
    assert(BLL.lists.filters.filter_elements([1, -2 + 2j, 2 + 2j, 6j], numbers.greater_than, 4) == [1, -2 + 2j, 2 + 2j])


def test_det_sum():
    assert(BLL.lists.operations.det_sum([], 1, 0) == 0)
    assert(BLL.lists.operations.det_sum([1 + 1j, 2 + 2j, 3, 4j], 1, 4) == 6 + 7j)
    assert(BLL.lists.operations.det_sum([-1, -5 + 3j, 3 - 5j], 1, 2) == -6 + 3j)


def test_get_imaginaries():
    imaginaries = BLL.lists.IO.get_imaginaries([], 1, 0)
    assert(imaginaries == [])

    imaginaries = BLL.lists.IO.get_imaginaries([1, 2, 3], 1, 3)
    assert(imaginaries == [0, 0, 0])

    imaginaries = BLL.lists.IO.get_imaginaries([1j, 2, 4j, -2 - 2j], 2, 4)
    assert(imaginaries == [0, 4, -2])

    imaginaries = BLL.lists.IO.get_imaginaries([-2j, -3j, 4j, 5j], 1, 4)
    assert(imaginaries == [-2, -3, 4, 5])


def test_duplicates():
    assert (BLL.lists.IO.duplicate([], 2 + 2j) == False)
    assert (BLL.lists.IO.duplicate([1, 2 + 2j, 3], 4j) == False)
    assert(BLL.lists.IO.duplicate([1, 2 + 2j, 3], 2 + 2j) == True)


def test_add_number():
    myList = [1j, 2, 4-5j]
    try:
        myList = BLL.lists.IO.add_number(myList, 10 + 2j)
        assert(myList == [1j, 2, 4-5j, 10+2j])
    except Exception as ex:
        assert(False)

    try:
        myList = BLL.lists.IO.add_number(myList, 4 - 5j)
        assert(False)
    except Exception as ex:
        assert(True)


def test_insert_number():
    myList = []
    try:
        myList = BLL.lists.IO.insert_number(myList, 2j, 1)
        assert(myList == [2j])
    except Exception as ex:
        assert(False)

    myList =[-2, -2j, 3, 4j]
    try:
        myList = BLL.lists.IO.insert_number(myList, 2j, 2)
        assert(myList == [-2, 2j, -2j, 3, 4j])
    except Exception as ex:
        assert(False)

    myList = [-2, -2j, 3, 4j]
    try:
        myList = BLL.lists.IO.insert_number(myList, -2j, 2)
        assert(False)
    except Exception as ex:
        assert(True)


def test_valid_position():
    assert(BLL.lists.IO.valid_position("5", 3) == False)
    assert(BLL.lists.IO.valid_position("5", 10) == True)
    assert(BLL.lists.IO.valid_position("-5", 10) == False)


def test_delete_numbers():
    try:
        newList = BLL.lists.IO.delete_numbers([], 1, 0)
        assert(False)
    except Exception as ex:
        assert(True)

    try:
        newList = BLL.lists.IO.delete_numbers([1, 2j, 3 + 4j, -5j], 1, 3)
        assert(newList == [-5j])
    except Exception as ex:
        assert(False)


def test_sort_list():
    try:
        sortedList = BLL.lists.sorting.sort_list([1, 1 + 2j, 5j, 3j, -100 + 100j], BLL.lists.sorting.imag_desc)
        assert(sortedList == [-100 + 100j, 5j, 3j, 1+2j, 1])
    except Exception as ex:
        assert(False)

    try:
        sortedList = BLL.lists.sorting.sort_list([], BLL.lists.sorting.imag_desc)
        assert(False)
    except Exception as ex:
        assert(True)


def test_valid_insert_position():
    assert(BLL.lists.IO.valid_insert_position("5", 3) == False)
    assert(BLL.lists.IO.valid_insert_position("5", 10) == True)
    assert(BLL.lists.IO.valid_insert_position("-5", 10) == False)
    assert(BLL.lists.IO.valid_insert_position("1", 0) == True)
    assert(BLL.lists.IO.valid_insert_position("10", 9) == True)


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
    """test_prime()
    test_filter_elements()
    test_det_sum()
    test_get_imaginaries()
    test_duplicates()
    test_add_number()
    test_insert_number()
    test_valid_position()
    test_valid_insert_position()
    test_delete_numbers()
    test_sort_list()"""
    test_validate_number()
