from utils import BaseMenu


class IsbnEditMenu(BaseMenu):
    header = \
        '''
         _____    _ _ _     _             ___ ____  ____  _   _ 
        | ____|__| (_) |_  | |__  _   _  |_ _/ ___|| __ )| \ | |
        |  _| / _` | | __| | '_ \| | | |  | |\___ \|  _ \|  \| |
        | |__| (_| | | |_  | |_) | |_| |  | | ___) | |_) | |\  |
        |_____\__,_|_|\__| |_.__/ \__, | |___|____/|____/|_| \_|
                                  |___/                                                           
        '''

    def __init__(self, root):
        super().__init__(title='ISBN', header=self.header, root=root)

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def execute(self):
        index = self.root.find_book_index(
            isbn=input('Enter the International Standard Book Number (ISBN): ')
        )

        self.previous_menu.list_update(index)
