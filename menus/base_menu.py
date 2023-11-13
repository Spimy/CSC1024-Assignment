import os


class BaseMenu:
    # Whether or not this is the root (main) menu
    # Used to determine whether to display the exit option or not
    root = False

    # Title of the menu used to be displayed in top-level menu
    title = None

    # Can be used to display ASCII art at the top of the menu
    header = None

    # List containing all submenus
    # This list should contain only objects that inherit BaseMenu
    sub_menus = []

    def __init__(self, title, root=False, header='', sub_menus=[]):
        '''
        Initialise the base menu object with provided arguments
        Only the title argument is required
        '''

        self.root = root
        self.title = title
        self.header = header
        self.sub_menus = sub_menus

    def _clear(self):
        '''
        Protected method used to clear the console
        This method can be used by child classes inherting from BaseMenu
        '''

        # If the user's computer is windows, then run the cls command
        # If the user's computer is UNIX based, then run the clear command
        # nt stands for New Technology (Windows NT)
        os.system('cls' if os.name == 'nt' else 'clear')

    def display(self):
        '''
        Display the submenus that the parent menu has
        '''

        # Clear the console before displaying
        self._clear()

        # Print the header of the menu
        print(self.header)

        # Map the sub menus list into a string with format: '[menu_number] menu_title'
        print('\n'.join(
            [f'[{i+1}] {menu.title}' for i, menu in enumerate(self.sub_menus)]
        ))

        # If this is the root menu, display the exit option
        if self.root:
            print(f'[{len(self.sub_menus) + 1}] Exit')

        # Return self so method calls can be chained
        return self

    def option_selection(self):
        option = int(input('Select menu: '))

        if self.root and option == len(self.sub_menus) + 1:
            # Exit the program with exit code 0 to indicate successful exit with no errors
            exit(code=0)

        # Display the selected menu
        self.sub_menus[option - 1].display()

        # Return self so method calls can be chained
        return self
