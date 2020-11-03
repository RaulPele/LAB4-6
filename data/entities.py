"""
Modul pentru crearea entitatilor de date utilizate de program
"""

from data.validation import validate_number
import BLL.lists.operations
import BLL.lists.IO

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

    @staticmethod
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

    @staticmethod
    def times(c1, c2):
        """
        Returneaza produsul dintre c1 si c2
        :param c1:  obiect Complex
        :param c2: obiect Complex
        :return: prod - obiect de tip Complex
        """

        prod = c1.copy_complex()
        real = prod.get_real() * c2.get_real() - prod.get_imag() * c2.get_imag()
        imag = prod.get_real() * c2.get_imag() + prod.get_imag() * c2.get_real()
        prod.set_real(real)
        prod.set_imag(imag)

        return prod

class ComplexOperations:
    """
    Contine o lista de numere complexe si o stiva cuprinzand istoricul
    operatiilor efectuate asupra listei
    """
    def __init__(self):
        self.__complexList = []
        self.__listStack = []

    def get_complexList(self):
        return self.__complexList

    def get_lastList(self):
        return self.__listStack[len(self.__listStack)-1]

    def get_complexListSize(self):
        return len(self.__complexList)

    def add_to_stack(self, list):
        self.__listStack.append(list)

    def set_complexList(self, list):
        if len(self.__listStack) == 0 or (
                not BLL.lists.operations.isEqual(self.get_complexList(), list)):
            self.add_to_stack(self.get_complexList())

        self.__complexList = BLL.lists.IO.copy_list(list)

    def undo(self):
        """
        Efectueaza operatia de undo asupra listei
        Reinitializeza lista cu ultima valoare din stiva
        Elimina valoarea din stiva
        :raise Exception: in caz ca asupra listei nu s-au efectuat operatii
        """
        if len(self.__listStack) == 0:
            raise Exception("Asupra listei nu s-au efectuat operatii de modificare.\n")

        self.__complexList = self.get_lastList()
        self.__listStack.pop()
