"""
Modulul contine functii pentru operatii si proprietati numerice.
"""

import math
from BLL.lists.IO import get_imag, get_real

def create_complex(real, imag):
    number = {"real": real, "imag": imag}
    return number


def is_prime(x):
    """
    Returneaza True daca numarul x este prim, False in caz contrar
    :param x: numar real
    :return True: daca x este prim
    :return False: daca x nu este prim
    """

    if x <= 1:
        return False
    if x % 2 == 0 and x != 2:
        return False

    div = 3
    while div * div <= x:
        if x % div == 0:
            return False
        div += 2
    return True


def less_than(x, compl):
    """
    Returneaza valoarea de adevar a propozitiei: modulul numarului complex
    compl este mai mic decat numarul x.
    :param x: numar real
    :param compl: numar complex
    :return: True - daca abs(compl)<x
            False - altfel
    """
    return module(compl) < x


def greater_than(x, compl):
    """
        Returneaza valoarea de adevar a propozitiei: modulul numarului complex
        compl este mai mare decat numarul x.
        :param x: numar real
        :param compl: numar complex
        :return: True - daca abs(compl)>x
                False - altfel
        """
    return x < module(compl)


def equal_to(x, compl):
    """
        Returneaza valoarea de adevar a propozitiei: modulul numarului complex
        compl este egal cu numarul x.
        :param x: numar real
        :param compl: numar complex
        :return: True - daca abs(compl) == x
                False - altfel
        """
    return x == module(compl)


def module(compl):
    return math.sqrt(get_real(compl) * get_real(compl) + get_imag(compl) * get_imag(compl))