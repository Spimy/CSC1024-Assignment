import os


class BaseMenu:
    # Whether or not this is the root (main) menu
    # Used to determine whether to display the exit option or not
    root = False

    # Save the previous menu used as a back option
    previous_menu = None

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

        if self.root:
            # If this is the root menu, display the exit option
            print(f'[{len(self.sub_menus) + 1}] Exit')
        else:
            # Otherwise display the back option
            print(f'[{len(self.sub_menus) + 1}] Back')

        # Return self so method calls can be chained
        return self

    def _option_input(self, display_string):
        '''
        Private method used to handle option inputs, making sure that the user
        inputs only integers and only within the allowed range
        '''

        # Option set to an invalid value by default to start the while loop
        option = 0

        # Flag to check if it has errored before to avoid displaying the same error message multiple times
        errored = False

        while option < 1 or option > len(self.sub_menus) + 1:
            try:
                # Try converting the input into an integer
                option = int(input(display_string))
            except ValueError:
                # If it failed to convert then handle the error
                if not errored:
                    # Set the errored flag to indicate that it had already errored
                    errored = True
                    # Update the display string to show the error message
                    display_string = f'[Must be an integer] {display_string}'
                continue

            # Update display string to show the range
            # This will only show if the input was out ouf range as if it is within range, the loop will not restart
            display_string = f'[Must be within 1-{len(self.sub_menus) + 1}] {display_string}'

        return option

    def option_selection(self):
        option = self._option_input('Select option: ')

        if option == len(self.sub_menus) + 1:
            # Exit the program with exit code 0 to indicate successful exit with no errors if root menu
            if self.root:
                exit(code=0)

            # If it is not a root menu, go back to previous menu
            self.previous_menu.display().option_selection()

        # Set the previous menu of the selected menu to current menu
        self.sub_menus[option - 1].previous_menu = self

        # Display the selected menu
        self.sub_menus[option - 1].display().option_selection()

        # Return self so method calls can be chained
        return self
