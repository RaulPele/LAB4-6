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
    #return math.sqrt(get_real(compl) * get_real(compl) + get_imag(compl) * get_imag(compl))
    pass


def isEqual(c1, c2):
    """
    Functia verifica daca doua obiecte Complex c1 si c2 sunt egale
    :param c1: obiect Complex
    :param c2: obiect Complex
    :return True: daca obiectele sunt egale
            False: daca obiectele nu sunt egale
    """

    if c1.get_real() == c2.get_real() and c1.get_imag() == c2.get_imag():
        return True
    return False
