from utils import BaseMenu, Utils


class DeleteMenu(BaseMenu):
    header = \
        '''
         _____                           _        __  __                  
        | ____|_  ____ _ _ __ ___  _ __ | | ___  |  \/  | ___ _ __  _   _ 
        |  _| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \ | |\/| |/ _ \ '_ \| | | |
        | |___ >  < (_| | | | | | | |_) | |  __/ | |  | |  __/ | | | |_| |
        |_____/_/\_\__,_|_| |_| |_| .__/|_|\___| |_|  |_|\___|_| |_|\__,_|
                                  |_|                                     
        '''

    def __init__(self, root):
        super().__init__(title='Delete Books', header=self.header, root=root)

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def selection(self):
        while True:
            isbn = input("Enter ISBN of book you wish to delete: ")
            index = Utils.find_book_index(
                book_list=self.root.book_list,
                isbn=isbn
            )

            if index != -1:
                print(f'Successfully deleted book with the ISBN "{isbn}."')
                del self.root.book_list[index]
            else:
                print(f'Book with ISBN "{isbn}" not found.')

            cont = ''
            while cont not in ('Y', 'N'):
                cont = input(
                    "Do you wish to delete another book (Y/N)?: "
                ).upper()

            if cont == "Y":
                self.display()

            elif cont == "N":
                self.root.display().selection()
                break
