from utils import BaseMenu


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
        super().__init__(title='Author and Title', header=self.header, root=root)

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def selection(self):
        index = self.root.find_book_index(
            author=input("Enter the Author's Name: "),
            title=input('Enter the Book Title: ')
        )

        self.previous_menu.list_update(index)
