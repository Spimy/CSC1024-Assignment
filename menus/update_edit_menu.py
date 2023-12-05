from utils import BaseMenu, Utils


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
        super().__init__(title='Update & Edit Books', header=self.header, root=root)

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def selection(self):
        # Menu to display options
        while True:
            # To test if the input is valid
            try:
                print('Please choose which information you would like to enter')
                print('[1] ISBN')
                print('[2] Author and title')
                print('[3] Back')

                choice = int(input("Select option: "))
            except:
                print('Invalid input! Please try again')
                choice = None

            if (choice == 1) or (choice == 2) or (choice == 3):
                break

        # Finding the index
        if choice == 1:
            index = Utils.find_book_index(
                book_list=self.root.book_list,
                isbn=input(
                    'Enter the International Standard Book Number (ISBN): '
                )
            )
        elif choice == 2:
            index = Utils.find_book_index(
                book_list=self.root.book_list,
                author=input("Enter the Author's Name: "),
                title=input('Enter the Book Title: ')
            )
        print(index)

        # Make update to the information
        self.list_update(index)

        # To return to the main menu
        input('Hit enter to go back to main menu...')
        self.root.display().selection()

    def list_update(self, index):
        # Display book that has been selected
        print('Here is information regarding the selected book:')
        print(self.root.book_list[index].to_string())

        print()

        print('Please choose what you want to edit:')
        print('[1] ISBN')
        print('[2] Author')
        print('[3] Title')
        print('[4] Publisher')
        print('[5] Genre')
        print('[6] Year Published')
        print('[7] Date of Purchase')
        print('[8] Status')

        edit_type = None
        while edit_type not in [1, 2, 3, 4, 5, 6, 7, 8]:
            try:
                edit_type = int(
                    input('Please enter what you would like to change:'))
            except:
                print('Invalid input! Please try again')
                pass

        # Change the information of the selected category
        if edit_type == 1:
            new_isbn = self.root.validator.input(
                display_string='Enter the new International Standard Book Number (ISBN): ',
                validator=self.root.validator.is_isbn
            )
            self.root.book_list[index].isbn = new_isbn

        elif edit_type == 2:
            first_name = self.root.validator.input(
                display_string="Enter the Author's new First Name: ",
                validator=self.root.validator.is_valid_string,
                error_msg='First Name should not consist a comma(s) or be empty'
            )
            surname = self.root.validator.input(
                display_string="Enter the Author's new Surname: ",
                validator=self.root.validator.is_valid_string,
                error_msg='Surname should not consist a comma(s) or be empty'
            )

            new_author = f"{first_name.title()} {surname.title()}"
            self.root.book_list[index].author = new_author

        elif edit_type == 3:
            new_title = self.root.validator.input(
                display_string='Enter the new Title of the Book: ',
                validator=self.root.validator.is_valid_string,
                error_msg='Title should not consist a comma(s) or be empty'
            )
            self.root.book_list[index].title = new_title

        elif edit_type == 4:
            new_publisher = self.root.validator.input(
                display_string='Enter the new Publisher: ',
                validator=self.root.validator.is_valid_string,
                error_msg='Publisher should not consist a comma(s) or be empty'
            )
            self.root.book_list[index].publisher = new_publisher

        elif edit_type == 5:
            new_genre = self.root.validator.input(
                display_string='Enter the new Genre: ',
                validator=self.root.validator.is_valid_string,
                error_msg='Genre should not consist a comma(s) or be empty'
            )
            self.root.book_list[index].genre = new_genre

        elif edit_type == 6:
            new_year_published = self.root.validator.input(
                display_string='Enter the new Year Published: ',
                validator=self.root.validator.is_valid_year
            )
            self.root.book_list[index].year_published = new_year_published

        elif edit_type == 7:
            new_date_purchased = self.root.validator.input(
                display_string='Enter the new Date Purchased: ',
                validator=self.root.validator.is_valid_date
            )
            self.root.book_list[index].date_purchased = new_date_purchased

        elif edit_type == 8:
            new_status = self.root.validator.input(
                display_string="Enter new Book Status ('to-read', 'reading', 'read'): ",
                validator=self.root.validator.is_allowed_status,
                error_msg='Invalid Status'
            )
            self.root.book_list[index].status = new_status

        # Display Updated Information
        print('The information has been updated!')
        print(self.root.book_list[index].to_string())


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

                # Format the Author + Title
                first_name = first_name[0].upper() + first_name[1:]
                surname = surname[0].upper() + surname[1:]
                name = f"{first_name} {surname}"
                title = title.title()
                break

        # Search list for the user to edit
        # Search for matching ISBN in list 
        if choice == 1: 
            while True: 
            

                # To display book details if found or to show that book cannot be found 
                if index != -1:
                    print("Here is informatio regarding the selected book:")
                    print(self.root.book_list[index].to_string()) 
                    break
                else:
                    print(f'Book with ISBN "{isbn}" not found.')


            print("Please choose what you want to edit: \nISBN \nAuthor \nTitle \nPublisher \nGenre \nYear of Publishing \nDate of Purchase \nStatus")
            edit_type = None 
            while edit_type not in ["ISBN", "Author", "Title", "Publisher", "Genre", "Year of Publishing", "Date of Purchase", "Status"]: 
                edit_type= input("Please enter what you would like to change: ")
                edit_type = edit_type.lower()

            if edit_type == "isbn": 
                new_isbn = input("Enter the new ISBN here: ")
                self.root.book_list[list_index].isbn = new_isbn

            elif edit_type == "author": 
                first_name = input("Please enter author first name: ")
                surname = input("Please enter author surname: ")
                first_name = first_name[0].upper() + first_name[1:]
                surname = surname[0].upper() + surname[1:]
                new_author = f"{first_name} {surname}"
                self.root.book_list[list_index].author = new_author 

            elif edit_type == "title":
                new_title = input("Enter the new tiltle here: ")
                self.root.book_list[list_index].title = new_title

            elif edit_type == "publisher": 
                new_publisher = input("Enter the new publisher here: ")
                self.root.book_list[list_index].publisher = new_publisher

            elif edit_type == "genre": 
                new_genre = input("Enter the new genre here: ")
                self.root.book_list[list_index].genre = new_genre

            elif edit_type == "year of publishing": 
                new_publishingyear = input("Enter the new year of publishing here: ")
                self.root.book_list[list_index].year_published = new_publishingyear

            elif edit_type == "date of purchase": 
                new_purchasedate = input("Enter the new year of date of purchase here: ")
                self.root.book_list[list_index].date_purchased = new_purchasedate

            elif edit_type == "status": 
                new_status = input("Enter the new status here: ")
                self.root.book_list[list_index].status = new_status

        elif choice == 2: 
            for index, book in enumerate(self.root.book_list): 
                if (book.author == name) and (book.title == title):
                    list_index = index
            
            # Display the information stored
            print(self.root.book_list[index].to_string()) 

            print("Please choose what you want to edit: \nISBN \nAuthor \nTitle \nPublisher \nGenre \nYear of Publishing \nDate of Purchase \nStatus")
            edit_type = None 
            while edit_type not in ["ISBN", "Author", "Title", "Publisher", "Genre", "Year of Publishing", "Date of Purchase", "Status"]: 
                edit_type= input("Please enter what you would like to change: ")
                edit_type = edit_type.lower()

            if edit_type == "isbn": 
                new_isbn = input("Enter the new ISBN here: ")
                self.root.book_list[list_index].isbn = new_isbn

            elif edit_type == "author": 
                first_name = input("Please enter author first name: ")
                surname = input("Please enter author surname: ")
                first_name = first_name[0].upper() + first_name[1:]
                surname = surname[0].upper() + surname[1:]
                new_author = f"{first_name} {surname}"
                self.root.book_list[list_index].author = new_author 

            elif edit_type == "title":
                new_title = input("Enter the new tiltle here: ")
                self.root.book_list[list_index].title = new_title

            elif edit_type == "publisher": 
                new_publisher = input("Enter the new publisher here: ")
                self.root.book_list[list_index].publisher = new_publisher

            elif edit_type == "genre": 
                new_genre = input("Enter the new genre here: ")
                self.root.book_list[list_index].genre = new_genre

            elif edit_type == "year of publishing": 
                new_publishingyear = input("Enter the new year of publishing here: ")
                self.root.book_list[list_index].year_published = new_publishingyear

            elif edit_type == "date of purchase": 
                new_purchasedate = input("Enter the new year of date of purchase here: ")
                self.root.book_list[list_index].date_purchased = new_purchasedate

            elif edit_type == "status": 
                new_status = input("Enter the new status here: ")
                self.root.book_list[list_index].status = new_status
'''


# self.root.book_list[0].isbn == inputisbn
# self.root.book_list[0].isbn == inputisbn
