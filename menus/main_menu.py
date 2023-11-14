from .base_menu import BaseMenu
from .example_menu import ExampleMenu


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
    book_list = []

    def __init__(self):
        super().__init__(
            title='Main Menu',
            header=self.header,
            sub_menus=[
                ExampleMenu(root=self)
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
                map(self._book_to_dict, file.read().splitlines())
            )

    def _exit(self, code):
        '''
        Override the exit method to save the books back to the text file before exiting
        '''
        with open('books_23020043.txt', 'w') as file:
            file.write('\n'.join(
                [','.join(book.values()) for book in self.book_list]
            ))
        super(MainMenu, self)._exit(code=code)

    def _book_to_dict(self, book):
        '''
        Private method to convert the read books read from the text file into a
        dictionary so that they are easier to work with
        '''

        book = book.split(',')

        return {
            'isbn': book[0],
            'author': book[1],
            'title': book[2],
            'publisher': book[3],
            'genre': book[4],
            'year_published': book[5],
            'data_purchased': book[6],
            'status': book[7],
        }
