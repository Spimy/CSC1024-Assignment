from utils import Book, BaseMenu
from .example_menu import ExampleMenu
from .display_menu import DisplayMenu


class MainMenu(BaseMenu):
    header = \
        '''
                          .--.                   .---.
                      .---|__|           .-.     |~~~|
                   .--|===|--|_          |_|     |~~~|--.
                   |  |===|  |'\     .---!~|  .--|   |--|
                   |%%|   |  |.'\    |===| |--|%%|   |  |
                   |%%|   |  |\.'\   |   | |__|  |   |  |
                   |  |   |  | \  \  |===| |==|  |   |  |
                   |  |   |__|  \.'\ |   |_|__|  |~~~|__|
                   |  |===|--|   \.'\|===|~|--|%%|~~~|--|
                   ^--^---'--^    `-'`---^-^--^--^---'--'
       ____              _      __  __                                   
      | __ )  ___   ___ | | __ |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
      |  _ \ / _ \ / _ \| |/ / | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
      | |_) | (_) | (_) |   <  | |  | | (_| | | | | (_| | (_| |  __/ |   
      |____/ \___/ \___/|_|\_\ |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                         |___/           
        '''

    # Books from the text file should be loaded into this list when the program starts
    # This list should be written to the file when the program ends
    book_list = []  # List of Book objects

    def __init__(self):
        super().__init__(
            title='Main Menu',
            header=self.header,
            sub_menus=[
                ExampleMenu(root=self),
                DisplayMenu(root=self)
            ]
        )
        self._load_books()

    def _load_books(self):
        '''
        Load books from the text file into the book_list list
        '''
        with open('books_23020043.txt', 'r') as file:
            self.book_list = list(
                # Convert book into a dictionary so it is easier to work with
                map(Book.from_string, file.read().splitlines())
            )

    def _exit(self, code):
        '''
        Override the exit method to save the books back to the text file before exiting
        '''
        with open('books_23020043.txt', 'w') as file:
            file.write(
                '\n'.join([book.to_string() for book in self.book_list])
            )
        super(MainMenu, self)._exit(code=code)
