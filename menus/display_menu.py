from utils import BaseMenu


class Colors:
    # ANSI escape codes for colors
    HEADER = '\033[95m'  # Purple/Pink
    OKBLUE = '\033[94m'  # Blue
    OKGREEN = '\033[92m'  # Green
    WARNING = '\033[93m'  # Yellow
    FAIL = '\033[91m'  # Red
    ENDC = '\033[0m'  # End Colour


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

    def selection(self):
        '''
        Main function to display the tabulated table and initiate book search if requested.
        '''
        headers = [
            'ISBN', 'Author', 'Title', 'Publisher',  'Genre', 'Year Published', 'Date Purchased', 'Status'
        ]

        # Calls the function load_data to get the book list
        book_data = self.load_books(self.root.book_list)

        # CALCULATIONS to find maximum length of each item in every column
        # Group headers and their respective datas(Asterisk to unpack data)
        column_widths = [
            max(len(str(item)) for item in column) for column in zip(headers, *book_data)
        ]

        # Group the headers and the calculated column widths
        # (^) to centre headers within respective column widths
        header_line = ' | '.join(
            f'{header:^{width}}' for header, width in zip(headers, column_widths)
        )

        # Calls function to start displaying the table and search function
        self.search_for_books(header_line, book_data, column_widths)
        return

    # Start of program
    def load_books(self, book_list):
        '''
        Load books from the book list database into a format suitable for display.
        '''
        # empty list to store books
        book_data = []
        # iterate through the list and add each books to the data list
        for book in book_list:
            book_data.append([
                book.isbn, book.author, book.title, book.publisher, book.genre, book.year_published, book.date_purchased, book.status
            ])

        # Returns new data with all books information
        return book_data

    def search_for_books(self, header_line, book_data, column_widths):
        '''
        A tabulated table will be displayed and it also prompts user whether to search for a book.
        '''
        while True:
            try:
                # Calls function to display tabulated table
                self.display_table(header_line, book_data, column_widths)

                print()

                user_choice = input(
                    'Do you want to search for books [Y/N]: '
                ).lower()

                # To handle errors if user does not answer 'Y' or 'N'
                while user_choice not in ('y', 'n'):
                    user_choice = input(
                        'Invalid Input, Do you want to search for books [Y/N]: '
                    ).lower()

                if user_choice == 'y':
                    while True:
                        print()

                        # Call the function to initiate search for books
                        results = self.search_books(
                            book_data, column_widths, header_line
                        )

                        if len(results) > 0:
                            self.display()  # To clear the terminal

                            print('Search Results:')
                            print()

                            self.display_table(
                                header_line, results, column_widths)
                        else:
                            print('No books found with the given search term.')

                        # Prompts user if they want to search for more books
                        user_search_choice = input(
                            'Do you wish to search for more books [Y/N]: '
                        ).lower()

                        # Handles the errors if the user does not answer 'Y' or 'N'
                        while user_search_choice not in ('y', 'n'):
                            user_search_choice = input(
                                'Invalid Input, do you wish to continue searching? [Y/N]: '
                            )

                        # Return to main menu after inputting 'n'
                        if user_search_choice != 'y':
                            self.root.display().selection()
                            break

                # if user inputs n, program will return to main menu
                elif user_choice == 'n':
                    self.root.display().selection()
                    break

            except KeyboardInterrupt:
                print('\nKeyboardInterrupt caught')
                self.display()
                continue

    def get_color_status(self, status):
        '''
        Takes the status column and returns it with appropriate colors based on its value.
        '''
        if status.lower() == 'to-read':
            # Prints 'to-read' status in red colour
            return (f'{Colors.FAIL}{status}{Colors.ENDC}')

        elif status.lower() == 'reading':
            # Prints 'reading' status in yellow colour
            return (f'{Colors.WARNING}{status}{Colors.ENDC}')

        elif status.lower() == 'read':
            # Prints 'read' status in green colour
            return (f'{Colors.OKGREEN}{status}{Colors.ENDC}')
        else:
            return status

    def display_table(self, header_line, book_data, column_widths):
        '''
        Display the tabulated table.
        '''

        print(header_line)
        print('-' * len(header_line))

        for row in book_data:

            # Create a list of formatted strings for each item in the row except the last one
            # This formatting is done for each string(isbn, author, title, etc...)
            # List will contain everything apart from Status column
            formatted_row = [
                f'{item:<{width}}' for item, width in zip(row[:-1], column_widths[:-1])
            ]

            # Calls the function to display the colours for status column
            status_colored = self.get_color_status(row[-1])

            # After adding colours, append every Status with the colours back into the columns
            formatted_row.append(f'{status_colored:<{column_widths[-1]}}')

            # Joins every string together as one with '|' as a seperator
            row_line = ' | '.join(formatted_row)
            print(row_line)

        print('-' * len(header_line))

    def search_books(self, book_data, column_widths, header_line):
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
        for row in book_data:

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
