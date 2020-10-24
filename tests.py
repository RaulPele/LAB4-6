"""
Modul de teste
"""
import numbers
import lists.operations
import lists.filters
import lists.IO

def test_prime():
    assert (numbers.is_prime(-7) == False)
    assert (numbers.is_prime(0) == False)
    assert (numbers.is_prime(1) == False)
    assert (numbers.is_prime(2) == True)
    assert (numbers.is_prime(11) == True)
    assert (numbers.is_prime(30) == False)
    

def test_filter_elements():
    assert(lists.filters.filter_elements([], numbers.is_prime) == [])
    assert(lists.filters.filter_elements([1, -2 + 2j, 2 + 2j, 6j], numbers.is_prime) == [1, -2+2j, 6j])
    assert(lists.filters.filter_elements([2+2j, 3,2, 7+5j], numbers.is_prime) == [])

    assert(lists.filters.filter_elements([1, -2+2j, 2+2j, 6j], numbers.less_than, 4) == [6j])
    assert(lists.filters.filter_elements([1, -2+2j, 2+2j, 6j], numbers.greater_than, 4) == [1, -2+2j, 2+2j])


def test_det_sum():
    assert(lists.operations.det_sum([], 1, 0) == 0)
    assert(lists.operations.det_sum([1 + 1j, 2 +2j, 3, 4j], 1, 4) == 6+7j)
    assert(lists.operations.det_sum([-1, -5+3j, 3-5j], 1, 2)==-6+3j)


def test_get_imaginaries():
    imaginaries = lists.IO.get_imaginaries([],1, 0)
    assert(imaginaries == [])

    imaginaries = lists.IO.get_imaginaries([1, 2, 3], 1, 3)
    assert(imaginaries == [0, 0, 0])

    imaginaries = lists.IO.get_imaginaries([1j, 2, 4j, -2-2j], 2, 4)
    assert(imaginaries == [0, 4, -2])

    imaginaries = lists.IO.get_imaginaries([-2j, -3j, 4j, 5j], 1, 4)
    assert(imaginaries == [-2, -3, 4, 5])


def test_duplicates():
    assert (lists.IO.duplicate([], 2+2j) == False)
    assert (lists.IO.duplicate([1, 2+2j, 3], 4j) == False)
    assert(lists.IO.duplicate([1, 2+2j, 3], 2+2j) == True)


def test_add_number():
    myList = [1j, 2, 4-5j]
    try:
        myList = lists.IO.add_number(myList, 10+2j)
        assert(myList == [1j, 2, 4-5j, 10+2j])
    except Exception as ex:
        assert(False)

    try:
        myList = lists.IO.add_number(myList, 4-5j)
        assert(False)
    except Exception as ex:
        assert(True)


def test_insert_number():
    myList = []
    try:
        myList = lists.IO.insert_number(myList, 2j, 1)
        assert(myList == [2j])
    except Exception as ex:
        assert(False)

    myList =[-2, -2j, 3, 4j]
    try:
        myList = lists.IO.insert_number(myList, 2j, 2)
        assert(myList == [-2, 2j, -2j, 3, 4j])
    except Exception as ex:
        assert(False)

    myList = [-2, -2j, 3, 4j]
    try:
        myList = lists.IO.insert_number(myList, -2j, 2)
        assert(False)
    except Exception as ex:
        assert(True)

def test_valid_position():
    assert(lists.IO.valid_position("5", 3) == False)
    assert(lists.IO.valid_position("5", 10) == True)
    assert(lists.IO.valid_position("-5", 10) == False)


def run_tests():
    test_prime()
    test_filter_elements()
    test_det_sum()
    test_get_imaginaries()
    test_duplicates()
    test_add_number()
    test_insert_number()
    test_valid_position()
