
class Menu:
    def __init__(self, menuItems, menuFunctions = None, subMenus = None):
        self.menuItems = menuItems
        self.menuFunctions = menuFunctions
        self.subMenus = subMenus

    def get_menuItems(self):
        return self.menuItems

    def get_menuFunctions(self):
        return self.menuFunctions

    def get_subMenus(self):
        return self.subMenus

    def get_subMenuAt(self, key):
        return (self.get_subMenus())[key]

    def print_menu(self):
        items = self.get_menuItems().values()
        for item in items:
            print(item)
        print()