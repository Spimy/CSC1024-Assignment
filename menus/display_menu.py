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

    def selection(self):
        headers = ["ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status"]
        
        #Empty list to store all the important information(isbn, author, title, etc...)
        data = []

        #To loop the entire book list until there is none
        for i in range(len(self.root.book_list)):

            #assigning them to their respective variable so it is easier to deal with
            isbn = self.root.book_list[i].isbn
            author = self.root.book_list[i].author
            title = self.root.book_list[i].title
            publisher = self.root.book_list[i].publisher
            genre = self.root.book_list[i].genre
            year_published = self.root.book_list[i].year_published
            date_purchased = self.root.book_list[i].date_purchased
            status = self.root.book_list[i].status

            #adding the individual variables above into the list
            data.append([isbn, author, title, publisher, genre, year_published, date_purchased, status])
        

        #Calculate all the column width and finding the maximum column length
        #Zip to store the headers list and data list into a single list
        #Asterisk(*) to unpack all the data
        column_widths = [max(len(str(item)) for item in column) for column in zip(headers, *data)]

        #(^) used to center the header within the column width
        #Zip to store the spacings of each width respectively
        header_line = " | ".join(f"{header:^{width}}" for header, width in zip(headers, column_widths))
        print(header_line)

        #print lines underneath so it looks cleaner
        print("-" * len(header_line))

        #to loop for how many rows there are in data
        for row in data:

            #to arrange all the "|" nicely within the list
            #zip to pair and store each row with its own respective column
            row_line = " | ".join(f"{item:<{width}}" for item, width in zip(row, column_widths))
            print(row_line)

        print("-" * len(header_line))


        #prompts user to input whether they want to search or return to main menu
        user_choice = input("Search Books[Y] or Return to Main Menu[N]:  ").lower()

        #if choices are incorrect, question will loop continously
        while user_choice not in ['y', 'n']:
            user_choice = input("Invalid Input, Search Books[Y] or Exit to Main Menu[N]: ").lower()

        if user_choice == 'y':
            while True:
                search_term = input("Search book by ISBN, AUTHOR, or TITLE(Type 'EXIT' to return to main menu):  ").lower()
                searched_books = []

                #if user enters exit, program will return to main menu
                if search_term =='exit'.lower():
                    self.root.display().selection()

                #for every row in data, if there are any terms matching the items in rows, add the entire row to a new list
                for row in data:
                    if any(search_term in str(item).lower() for item in row):
                        searched_books.append(row)

                #checks whether search_books list is empty,
                if len(searched_books) > 0:
                    print("\nSearch Results:")

                    #print headers with '-' to make it look cleaner
                    print(header_line)
                    print("-" * len(header_line))

                    #for the book found in the new list called searched_books
                    for book in searched_books:
                        
                        #to arrange all the "|" nicely within the list
                        #zip to pair the book with its own respective column_widths
                        print(" | ".join(f"{item:<{width}}" for item, width in zip(book, column_widths)))

                    #print lines underneath so it looks cleaner
                    print("-" * len(header_line))
                          
                else:
                    print("No books found with the given search term.")
                    #continues the program if no books are found
                    continue

        #if user enters n, program will return to main menu                     
        if user_choice.lower() == 'n':
            self.root.display().selection()

