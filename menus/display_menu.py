from utils import BaseMenu


class DisplayMenu(BaseMenu):
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
        super().__init__(title='Display Books', header=self.header, root=root)

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def selection(self):
        for i in range(len(self.root.book_list)):
            print(f'[{i + 1}] Book: {self.root.book_list[i].title}')


class BookDisplay:
    def __init__(self):
        self.book_file = 'books_23020043.txt'

    def display_book(self):
        with open(self.book_file, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start = 1):
                print(f"{i}. {line.strip()}")

        input('Hit enter to go back to main menu...')
        self.root.display().selection()

if __name__ == "__main__":
    display = BookDisplay()
    display.display_book()


