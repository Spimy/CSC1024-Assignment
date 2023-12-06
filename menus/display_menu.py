from utils import BaseMenu, Validator, DisplayHelper


class DisplayMenu(BaseMenu):
    header = \
        '''
__________               __     .____    ._____.                               
\______   \ ____   ____ |  | __ |    |   |__\_ |______________ _______ ___.__. 
 |    |  _//  _ \ /  _ \|  |/ / |    |   |  || __ \_  __ \__  \\_  __ <   |  | 
 |    |   (  <_> |  <_> )    <  |    |___|  || \_\ \  | \// __ \|  | \/\___  | 
 |______  /\____/ \____/|__|_ \ |_______ \__||___  /__|  (____  /__|   / ____| 
        \/                   \/         \/       \/           \/       \/                                  
       
         '''

    def __init__(self, root):
        super().__init__(title='Display Books', header=self.header, root=root)

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def execute(self):
        '''
        Main function to display the tabulated table and initiate book search if requested.
        '''
        # Flatten the book list to contain only lists of book attributes
        flattened_book_list = self.root.flatten_book_list()

        # Display all books in the database
        DisplayHelper.display_table(flattened_book_list)
        print()  # Print empty line

        # Start search loop
        while True:
            continue_search = Validator.input(
                display_string='Do you wish to search for books (Y/N)?: ',
                validator=Validator.is_valid_confirmation
            ).upper()

            # If user does not want to search for books then exit the search loop
            if continue_search == 'N':
                break

            # Search for books
            results = self.search_books(flattened_book_list)

            # Tabulate the results and print them if there are results
            if len(results) > 0:
                self.display()  # To clear the terminal

                print('Search Results:')
                print()

                DisplayHelper.display_table(results)
            else:
                print('No books found with the given search term.')

            print()

        # Go back to main menu if broken out of the search loop
        self.root.display().execute()

    def search_books(self, flattened_book_list):
        '''
        Search for books based on ISBN, AUTHOR, and TITLE.
        '''

        # Empty list to store the row/s of books searched
        searched_books = []

        isbn_search = input('Enter ISBN: ').lower()
        author_search = input('Enter author name: ').lower()
        title_search = input('Enter book title: ').lower()

        print()

        # Loop through rows in the database
        for row in flattened_book_list:

            # Extract ISBN, AUTHOR, and TITLE from the row
            row_isbn, row_author, row_title = row[:3]

            # Check if the search terms match
            # This part of the code will check if either one is similar and display it
            isbn_match = isbn_search.lower() in row_isbn.lower()
            # For example, even if isbn, author and title are all from different books, it will display all 3
            author_match = author_search.lower() in row_author.lower()
            # To search for a specific book, all 3 information must be accurate and
            title_match = title_search.lower() in row_title.lower()

            # If any of the search terms match, add the row to the results
            if isbn_match or author_match or title_match:
                searched_books.append(row)

        return searched_books
