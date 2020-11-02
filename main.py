# module imports
from ui.console import run
from utils.tests import run_tests
def callFunction(myList):
    myList = [1, 2] +[2, 3]
    print(myList)

def test():
    myList = [1, 2]
    callFunction(myList)
    print(myList)
# apel functii
if __name__ == "__main__":
    run_tests()
    run()
    #print((1+2j)*(1+3j)*(1+2j))


