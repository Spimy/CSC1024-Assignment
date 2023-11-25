from utils import BaseMenu

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

    def display_data(self, data, column_widths):
        # Display each row of data using for loop
        for row in data:
            self.display_row(row, column_widths)

    def display_row(self, row, column_widths):
        # Create a formatted string for a single row by pairing each item in row within their own respective column
        row_line = " | ".join(f"{item:<{width}}" for item, width in zip(row, column_widths))
        print(row_line)

    def tabulated_table(self, header_line, data, column_widths):
        # Display the header line and table body
        print(header_line)
        print("-" * len(header_line))
        
        # Calls the function to display every data in a table
        self.display_data(data, column_widths)

        print("-" * len(header_line))

    def searched_results(self, search_term, data, column_widths, header_line):
        #empty list to store search functions
        searched_books = []

        if search_term:
            # Search for the given term in ISBN, AUTHOR, or TITLE
            for row in data:
                isbn, author, title = row[:3]
                if search_term in isbn.lower() or search_term in author.lower() or search_term in title.lower():
                    searched_books.append(row)

            if searched_books:
                # Display search results if there are matches
                print("\nSearch Results:")
                print(header_line)
                print("-" * len(header_line))
                self.display_data(searched_books, column_widths)
                print("-" * len(header_line))
            else:
                print("No books found with the given search term.")
        else:
            print("Please search for a book by ISBN, Author, or Title.")

    def selection(self):
        headers = ["ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status"]
        # Load all new book data from function load_data()
        data = self.load_data()

        # Asterisk to unpack the data
        # Calculate maximum length of each item in their column
        # zip headers and column width to pair 
        # (^) to center each headers with their own column width
        column_widths = [max(len(str(item)) for item in column) for column in zip(headers, *data)] #CALCULATING COLUMN WIDTH ONLY
        header_line = " | ".join(f"{header:^{width}}" for header, width in zip(headers, column_widths)) #ONLY FOR HEADERS

        # Calls the function to tabulate the table
        self.tabulated_table(header_line, data, column_widths)

        # Prompts user to search or return to main menu
        user_choice = input("Search Books[Y] or Return to Main Menu[N]: ").lower()

        #handles if the input are not correct
        while user_choice not in ['y', 'n']:
            user_choice = input("Invalid Input, Search Books[Y] or Exit to Main Menu[N]: ").lower()

        if user_choice == 'y':
            while True:
                search_term = input("Search book by ISBN, AUTHOR, or TITLE (Type 'EXIT' to return to the main menu): ").lower()
                if search_term == 'exit':
                    # Return to the main menu if the user chooses to exit the search
                    self.root.display().selection()
                    break

                #
                self.searched_results(search_term, data, column_widths, header_line)

        elif user_choice == 'n':
            # Return to the main menu if the user chooses not to search
            self.root.display().selection()

            return
        
    #Start of function
    def load_data(self):
        # Load data from the root's book_list and format it into a list
        data = []
        for i in range(len(self.root.book_list)): #adds every information in book_list into data
            book = self.root.book_list[i]
            data.append([book.isbn, book.author, book.title, book.publisher, book.genre, book.year_published, book.date_purchased, book.status])

        #new data called will contain all book information
        return data