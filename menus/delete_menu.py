from utils import BaseMenu


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
        isbn = input("Enter ISBN of book you wish to delete: ")
        index = self.find_book_index(isbn)
        if index != -1:
            del self.root.book_list[index]
        self.root.display().selection()



    def find_book_index(self, target_isbn):
        for index, book in enumerate(self.root.book_list):
            if book.isbn == target_isbn:
                return index
        return -1  # Return -1 if the ISBN is not found in the list

   

    

    
