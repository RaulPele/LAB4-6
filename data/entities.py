"""
Modul pentru crearea entitatilor de date utilizate de program
"""


class Complex:
    """
    Numerele complexe sunt reprezentate sub forma de obiecte de tip Complex
    """
    # constante
    REAL = "real"
    IMAGINARY = "imag"

    def __init__(self, real=None, imaginary=None):
        self.number = {Complex.REAL: real, Complex.IMAGINARY: imaginary}

    def get_real(self):
        return self.number[Complex.REAL]

    def get_imag(self):
        return self.number[Complex.IMAGINARY]

    def get_complex_string(self):
        """Formateaza dictionarul care reprezinta numarul complex
        in forma a+bj pentru afis
        :return numStr: numarul complex sub forma de string"""

        imag = self.get_imag()
        if imag >= 0:
            numStr = str(self.get_real()) + " + " + str(self.get_imag()) + "j"
        else:
            numStr = str(self.get_real()) + " - " + str(-self.get_imag()) + "j"


        return numStr

    def copy_complex(self):
        """
        Returneaza o copie a obiectului self
        :return copy: copia obiectului self
        """
        return Complex(self.get_real(), self.get_imag())
