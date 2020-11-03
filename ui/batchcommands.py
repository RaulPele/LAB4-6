from data.entities import Complex
import BLL.lists.IO
import BLL.lists.sorting
from data.validation import validate_position, validate_command
import ui.console
from ui.menu import  Menu


def add_command(complexOp, args=None):
    try:
        number = complex(args)
    except ValueError:
        print("Argument invalid\n")
    else:
        compl = Complex(number.real, number.imag)
        myList = complexOp.get_complexList()
        myList = BLL.lists.IO.add_number(myList, compl)
        complexOp.set_complexList(myList)
        ui.console.print_seq_complex(myList, 0, len(myList), "Lista rezultata: \n")


def delete_command(complexOp, args = None):

    try:
        validate_position(args, complexOp.get_complexListSize())
    except ValueError:
        print("Argument invalid\n")
    else:
        pos = int(args)
        myList = complexOp.get_complexList()
        myList = BLL.lists.IO.delete_numbers(myList, pos, pos)
        complexOp.set_complexList(myList)
        ui.console.print_seq_complex(myList, 0, len(myList), "Lista rezultata: \n")


def print_command(complexOp, args = None):
    if args != "imag":
        print("Argument invalid")
        return

    myList = BLL.lists.IO.copy_list(complexOp.get_complexList())
    myList = BLL.lists.sorting.sort_list(myList, BLL.lists.sorting.imag_desc)
    ui.console.print_seq_complex(myList, 0, len(myList), "Lista rezultata: \n")


def getCommand(cmd):
    commands = Menu.get_commands()
    #cmd args
    currentCmd = cmd.split(" ")
    try:
        validate_command(currentCmd[0], list(commands.keys()))
    except Exception as ex:
        print(str(ex))
        return
    if len(currentCmd)>1:
        return Menu.get_commandAt(currentCmd[0]), currentCmd[1]
    return Menu.get_commandAt(currentCmd[0]), None


def interpretCommands(complexOp, op):
    userCmds = op.split(";")
    for cmd in userCmds:
        try:
            command, arg= getCommand(cmd)
        except Exception as ex:
            print("Comanda " + cmd+ " este invalida!\n")
        else:
            command(complexOp, arg)

