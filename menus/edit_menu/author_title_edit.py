from utils import BaseMenu, Validator


class AuthorTitleEditMenu(BaseMenu):
    header = \
        '''
                             _____    _ _ _     _                                   
                            | ____|__| (_) |_  | |__  _   _                         
                            |  _| / _` | | __| | '_ \| | | |                        
                            | |__| (_| | | |_  | |_) | |_| |                        
         _____ _ _   _      |_____\__,_|_|\__|_|_.__/_\__, |   _   _                
        |_   _(_) |_| | ___    __ _ _ __   __| |    / \___/  _| |_| |__   ___  _ __ 
          | | | | __| |/ _ \  / _` | '_ \ / _` |   / _ \| | | | __| '_ \ / _ \| '__|
          | | | | |_| |  __/ | (_| | | | | (_| |  / ___ \ |_| | |_| | | | (_) | |   
          |_| |_|\__|_|\___|  \__,_|_| |_|\__,_| /_/   \_\__,_|\__|_| |_|\___/|_|                               
        '''

    def __init__(self, root):
        super().__init__(title='Edit by Author and Title', header=self.header, root=root)

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def execute(self):
        while True:
            index = self.root.find_book_index(
                author=input("Enter the Author's Name: "),
                title=input('Enter the Book Title: ')
            )

            # If index is not -1 then that means a book was found so exit the loop
            if index != -1:
                break

            print('No book found from the Author and Title provided.')
            print()

        while True:
            self.previous_menu.list_update(index)

            # Allow user to edit the book again or go back to the previous menu
            cont = Validator.input(
                display_string='Do you wish to edit the book again (Y/N)?: ',
                validator=Validator.is_valid_confirmation
            ).upper()

            if cont == 'Y':
                self.display()

            elif cont == 'N':
                self.previous_menu.display().execute()
                break
