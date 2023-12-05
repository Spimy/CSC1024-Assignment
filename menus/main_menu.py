from utils import Book, BaseMenu
from .example_menu import ExampleMenu
from .display_menu import DisplayMenu
from .add_menu import AddMenu
from .update_edit_menu import UpdateMenu
from .delete_menu import DeleteMenu


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
                DisplayMenu(root=self),
                AddMenu(root=self),
                UpdateMenu(root=self),
                DeleteMenu(root=self)
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
                '\n'.join([str(book) for book in self.book_list])
            )
        super()._exit(code=code)

    def find_book_index(self, **kwargs):
        '''
        Find the index of a book based on the attribute passed through the kwargs parameter
        Returns -1 if no book is found
        '''

        num_match = 0

        # Check if the key and attributes match to return the correct index
        for index, book in enumerate(self.book_list):
            for key in kwargs.keys():
                # If attribute does not match value then skip the current key
                if getattr(book, key, '').lower() != kwargs[key].lower():
                    break

                # Make sure all attributes match the values from kwargs
                num_match += 1
                if num_match == len(kwargs.keys()):
                    return index

            num_match = 0

        return -1
