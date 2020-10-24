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
    pass


def run_tests():
    test_prime()
    test_filter_elements()
    test_det_sum()
