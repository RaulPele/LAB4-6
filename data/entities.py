"""
Modul pentru crearea entitatilor de date utilizate de program
"""


class Complex:
    """
    Numerele complexe sunt reprezentate sub forma de obiecte de tip Complex
    """
    #constante
    REAL = "real"
    IMAGINARY = "imag"

    def __init__(self, real=None, imaginary=None):
        self.number = {Complex.REAL: real, Complex.IMAGINARY: imaginary}

    def get_real(self):
        return self.number[Complex.REAL]

    def get_imag(self):
        return self.number[Complex.IMAGINARY]

    
