"""
Modul pentru crearea entitatilor de date utilizate de program
"""

from data.validation import validate_number


class Complex:
    """
    Numerele complexe sunt reprezentate sub forma de obiecte de tip Complex
    """
    # constante
    REAL = "real"
    IMAGINARY = "imag"

    def __init__(self, real=None, imaginary=None):
        self.__number = {Complex.REAL: real, Complex.IMAGINARY: imaginary}

    def get_real(self):
        return self.__number[Complex.REAL]

    def get_imag(self):
        return self.__number[Complex.IMAGINARY]

    def set_real(self, value):
        try:
            validate_number(value, float)
        except ValueError as ex:
            raise ValueError(str(ex))
        else:
            self.__number[Complex.REAL] = value

    def set_imag(self, value):
        try:
            validate_number(value, float)
        except ValueError as ex:
            raise ValueError(str(ex))
        else:
            self.__number[Complex.IMAGINARY] = value

    def get_complex_string(self):
        """Formateaza dictionarul care reprezinta numarul complex
        in forma a+bj pentru afis
        :return numStr: numarul complex sub forma de string"""

        imag = self.get_imag()
        real = self.get_real()
        numStr = ""

        if real is not None:
            numStr += str(real)

        if imag is not None:
            if imag >= 0:
                numStr += "+" + str(imag) + "j"
            else:
                numStr += "-" + str(-imag) + "j"

        return numStr

    def copy_complex(self):
        """
        Returneaza o copie a obiectului self
        :return copy: copia obiectului self
        """
        return Complex(self.get_real(), self.get_imag())

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

    