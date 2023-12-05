from utils import BaseMenu, Validator


class DeleteMenu(BaseMenu):
    header = \
        '''
         ____       _      _         ____              _        
        |  _ \  ___| | ___| |_ ___  | __ )  ___   ___ | | _____ 
        | | | |/ _ \ |/ _ \ __/ _ \ |  _ \ / _ \ / _ \| |/ / __|
        | |_| |  __/ |  __/ ||  __/ | |_) | (_) | (_) |   <\__ \\
        |____/ \___|_|\___|\__\___| |____/ \___/ \___/|_|\_\___/                         
        '''

    def __init__(self, root):
        super().__init__(title='Delete Books', header=self.header, root=root)

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def selection(self):
        while True:
            isbn = input("Enter ISBN of book you wish to delete: ")
            index = self.root.find_book_index(
                isbn=isbn
            )

            if index != -1:
                print(f'Successfully deleted book with the ISBN "{isbn}".')
                del self.root.book_list[index]
            else:
                print(f'Book with ISBN "{isbn}" not found.')

            print()

            # Allow user to delete another book or go back to main menu
            cont = Validator.input(
                display_string='Do you wish to delete another book (Y/N)?: ',
                validator=Validator.is_valid_confirmation
            ).upper()

            if cont == 'Y':
                # Clear the console and display the header again
                self.display()

            elif cont == 'N':
                self.root.display().selection()
                break
