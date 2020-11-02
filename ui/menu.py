
class Menu:
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

    def get_menuReturnFunctions(self):
        if self.get_menuFunctions() == None:
            return None
        return self.get_menuFunctions()["return"]

    def get_menuNoReturnFunctions(self):
        if self.get_menuFunctions() == None:
            return None
        return self.get_menuFunctions()["noreturn"]

    def get_functionAt(self, functions, index):
        return functions[index]

    def print_menu(self):
        items = self.get_menuItems().values()
        for item in items:
            print(item)
        print()

