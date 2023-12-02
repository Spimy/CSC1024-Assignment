from utils import BaseMenu

class UpdateMenu(BaseMenu):
    header = \
        '''
         _____                           _        __  __                  
        | ____|_  ____ _ _ __ ___  _ __ | | ___  |  \/  | ___ _ __  _   _ 
        |  _| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \ | |\/| |/ _ \ '_ \| | | |
        | |___ >  < (_| | | | | | | |_) | |  __/ | |  | |  __/ | | | |_| |
        |_____/_/\_\__,_|_| |_| |_| .__/|_|\___| |_|  |_|\___|_| |_|\__,_|
                                  |_|                                     
        '''
    
    error_flags = {
        'isbn': {
            'valid': False,
            'message': ''
        },
        'first_name': False,
        'surname': False,
        'title': False,
        'publisher': False,
        'genre': False,
        'year_published': {
            'valid': False,
            'message': ''
        },
        'date_purchased': {
            'valid': False,
            'message': ''
        },
        'status': False
    }


    def __init__(self, root):
        super().__init__(title='Update & Edit Books', header=self.header, root=root
        )

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def selection(self):
        # Start coding from here
        '''
        Check the ISBN or Author & Title 

        > If matching records are found, the user is prompted to enter
        new information for the book 

        > User shouls be able to handle either single or multiple books at once

        ** Use while loop to allow user to be able to change value again 
        '''

        # Menu to display options 
        while True: 
             # To test if the input is valid
            try: 
                print("Please choose which information you would like to enter")
                print("[1] ISBN \n[2] Author and title")
                choice = int(input("Please choose either option 1 or option 2: "))
            except: 
                print("Invalid input! Please try again")
                choice = None

            if (choice == 1) or (choice == 2): 
                break 

        # Prompt user for the ISBN or Author + Title 
        # ISBN
        if choice == 1: 
            # User input isbn and check validity
            while True:
                isbn = input(
                    f"{self.error_flags['isbn']['message'] if not self.error_flags['isbn']['valid'] else ''}Enter the International Standard Book Number (ISBN): "
                )

                # User may input isbn with dashes or spaces
                # This should be removed before function is run
                isbn = isbn.replace("-", "").replace(" ", "").upper()

                # Function from validator.py should check validity of isbn
                self.error_flags['isbn'] = self.root.validator.is_isbn(isbn)

                # If valid then no need to ask for inout again
                if self.error_flags['isbn']['valid']:
                    break
        # Author & Title
        elif choice == 2: 
            while True: 
                # User input Author & Title and check validity
                # Author First Name 
                while True:
                    first_name = input(
                        f"{'[First Name should not consist a comma(s) or be empty] ' if self.error_flags['first_name'] else ''}Enter the Author's First Name: "
                    )

                    # Guard Clause - if first_name is valid then break
                    # If not valid - set error_flag to true
                    if self.root.validator.is_valid_string(first_name):
                        break

                    self.error_flags['first_name'] = True
                # Author Surname 
                while True:
                    surname = input(
                        f"{'[Surname should not consist a comma(s) or be empty] ' if self.error_flags['surname'] else ''}Enter the Author's Surname: "
                    )

                    # Guard Clause - if surname is valid then break
                    # If not valid - set error_flag to true
                    if self.root.validator.is_valid_string(surname):
                        break

                    self.error_flags['surname'] = True
                # Allow user to input Title name
                while True:
                    title = input(
                        f"{'[Title should not consist a comma(s) or be empty] ' if self.error_flags['title'] else ''}Enter the Title of the Book: "
                    )

                    # Guard Clause - if title is valid then break
                    # If not valid - set error_flag to true
                    if self.root.validator.is_valid_string(title):
                        break

                    self.error_flags['title'] = True

                # Format the ISBN or Author + Title
                first_name = first_name[0].upper() + first_name[1:]
                surname = surname[0].upper() + surname[1:]
                title = title[0].upper() + title[1:]

        # Search list for the user to edit
        # Search for matching ISBN in list 
        if choice == 1: 
            for index, book in enumerate(self.root.book_list): 
                if book.isbn == isbn:
                    list_index = index
            # Display the information stored
            print(self.root.book_list[index].to_string()) 

            print("Please choose what you want to edit: \nISBN \nAuthor \nTitle \nPublisher \nGenre \nYear of Publishing \nDate of Purchase \nStatus")
            edit_type = None 
            while edit_type not in ["ISBN", "Author", "Title", "Publisher", "Genre", "Year of Publishing", "Date of Purchase", "Status"]: 
                edit_type= input("Please enter what you would like to change: ")

            if edit_type == "ISBN": 
                new_isbn = input("Enter the new ISBN here: ")
                self.root.book_list[list_index].isbn = new_isbn

            elif edit_type == "Author": 
                first_name = input("Please enter author first name: ")
                surname = input("Please enter author surname: ")
                first_name = first_name[0].upper() + first_name[1:]
                surname = surname[0].upper() + surname[1:]
                new_author = f"{first_name} {surname}"
                self.root.book_list[list_index].author = new_author 

            elif edit_type == "Title":
                new_title = input("Enter the new tiltle here: ")
                self.root.book_list[list_index].title = new_title

            elif edit_type == "Publisher": 
                new_publisher = input("Enter the new publisher here: ")
                self.root.book_list[list_index].title = new_publisher

            elif edit_type == "Genre": 
                new_genre = input("Enter the new genre here: ")
                self.root.book_list[list_index].title = new_genre

            elif edit_type == "Year of Publishing": 
                new_publishingyear = input("Enter the new year of publishing here: ")
                self.root.book_list[list_index].title = new_publishingyear

            elif edit_type == "Date of Purchase": 
                new_purchasedate = input("Enter the new year of date of purchase here: ")
                self.root.book_list[list_index].title = new_purchasedate

            elif edit_type == "Status": 
                new_status = input("Enter the new status here: ")
                self.root.book_list[list_index].title = new_status

        elif choice == 2: 
            pass



    # Update the information 





# To return to the main menu 
        input('Hit enter to go back to main menu...')
        self.root.display().selection()


# self.root.book_list[0].isbn == inputisbn
# self.root.book_list[0].isbn == inputisbn
