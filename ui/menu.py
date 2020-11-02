
class Menu:

    __menuStack=[]

    def __init__(self, menuItems, menuFunctions = None, subMenus = None):
        self.__menuItems = menuItems
        self.__menuFunctions = menuFunctions
        self.__subMenus = subMenus

    def get_menuItems(self):
        return self.__menuItems

    def get_menuFunctions(self):
        return self.__menuFunctions

    def get_subMenus(self):
        return self.__subMenus

    def get_subMenuAt(self, key):
        return (self.get_subMenus())[key]


    def get_functionAt(self, functions, index):
        return functions[index]

    def print_menu(self):
        items = self.get_menuItems().values()
        for item in items:
            print(item)
        print()

    @staticmethod
    def user_exits(op):
        menuItems = Menu.get_currentMenu().get_menuItems()
        if int(op) == len(menuItems.keys()):
            return True
        return False

    @staticmethod
    def navigate_backwards():
        if len(Menu.__menuStack) > 0:
            Menu.__menuStack.pop()

    @staticmethod
    def get_currentMenu():
        currentMenu = Menu.__menuStack[len(Menu.__menuStack) - 1]
        return currentMenu

    @staticmethod
    def navigate_to_submenu(op):
        currentMenu = Menu.get_currentMenu()
        Menu.__menuStack.append(currentMenu.get_subMenuAt(op))

    @staticmethod
    def __get_menuStack():
        return Menu.__menuStack

    @staticmethod
    def get_stack_size():
        return len(Menu.__menuStack)

    @staticmethod
    def initialize_stack(mainMenu):
        if len(Menu.__menuStack) == 0:
            Menu.__menuStack.append(mainMenu)


