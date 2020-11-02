"""
Modulul contine functii pentru operatii si proprietati numerice.
"""

import math


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
    :param compl: obiect Complex
    :return: True - daca abs(compl)<x
            False - altfel
    """
    return module(compl) < x


def greater_than(x, compl):
    """
        Returneaza valoarea de adevar a propozitiei: modulul numarului complex
        compl este mai mare decat numarul x.
        :param x: numar real
        :param compl: obiect Complex
        :return: True - daca abs(compl)>x
                False - altfel
        """
    return x < module(compl)


def equal_to(x, compl):
    """
        Returneaza valoarea de adevar a propozitiei: modulul numarului complex
        compl este egal cu numarul x.
        :param x: numar real
        :param compl: obiect Complex
        :return: True - daca abs(compl) == x
                False - altfel
        """
    return x == module(compl)


def module(compl):
    """
    Returneaza modulul unui numar complex
    :param compl: obiect Complex
    :return : modulul lui compl
    """
    return math.sqrt(compl.get_real() * compl.get_real() + compl.get_imag() * compl.get_imag())


