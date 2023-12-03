from utils import BaseMenu, Book


class AddMenu(BaseMenu):
    header = \
        '''
            _       _     _   ____              _    
           / \   __| | __| | | __ )  ___   ___ | | __
          / _ \ / _` |/ _` | |  _ \ / _ \ / _ \| |/ /
         / ___ \ (_| | (_| | | |_) | (_) | (_) |   < 
        /_/   \_\__,_|\__,_| |____/ \___/ \___/|_|\_\                                  
        '''

    def __init__(self, root):
        super().__init__(title='Add Books', header=self.header, root=root)

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def selection(self):
        '''
        Allow user to input all book details and add it to the list
        Check for errors and allow user to re-input details if needed
        '''

        while True:
            isbn = self.validator_input(
                display_string='Enter the International Standard Book Number (ISBN): ',
                validator=self.root.validator.is_isbn
            )
            first_name = self.validator_input(
                display_string="Enter the Author's First Name: ",
                validator=self.root.validator.is_valid_string,
                error_msg='First Name should not consist a comma(s) or be empty'
            )
            surname = self.validator_input(
                display_string="Enter the Author's Surname: ",
                validator=self.root.validator.is_valid_string,
                error_msg='Surname should not consist a comma(s) or be empty'
            )
            title = self.validator_input(
                display_string="Enter the Title of the Book: ",
                validator=self.root.validator.is_valid_string,
                error_msg='Title should not consist a comma(s) or be empty'
            )
            publisher = self.validator_input(
                display_string="Enter the Publisher: ",
                validator=self.root.validator.is_valid_string,
                error_msg='Publisher should not consist a comma(s) or be empty'
            )
            genre = self.validator_input(
                display_string="Enter the Genre: ",
                validator=self.root.validator.is_valid_string,
                error_msg='Genre should not consist a comma(s) or be empty'
            )
            year_published = self.validator_input(
                display_string='Enter the Year Published: ',
                validator=self.root.validator.is_valid_year
            )
            date_purchased = self.validator_input(
                display_string='Enter the Date Purchased: ',
                validator=self.root.validator.is_valid_date
            )
            status = self.validator_input(
                display_string="Enter Book Status ('to-read', 'reading', 'read'): ",
                validator=self.root.validator.is_allowed_status,
                error_msg='Invalid Status'
            )

            # Convert inputs to title casing
            author = f'{first_name} {surname}'.title()
            title = title.title()
            publisher = publisher.title()
            genre = genre.title()

            # Create new book
            # Concatenate first_name and surname using f string
            book = Book(
                isbn, f"{first_name} {surname}", title, publisher, genre, year_published, date_purchased, status
            )
            self.root.book_list.append(book)

            # Reassure user that book has been added
            print("Book has successfully been added!")
            print()

            # Allow user to add another book or go back to main menu
            cont = ''
            while cont.upper() not in ('Y', 'N'):
                cont = input("Do you wish to add another book (Y/N)?: ")

            if cont.upper() == "Y":
                self.display()

            elif cont.upper() == "N":
                self.root.display().selection()
                break

    def validator_input(self, display_string, validator, error_msg=''):
        '''
        Prompt user for input and validate it before returning a value
        display_string - string to display when asking for user input
        validator - callback function to use to validate user input
        error_msg - optional parameter, the error message to display when validator returns a boolean
        '''
        display = display_string

        while True:
            user_input = input(display)
            validator_result = validator(user_input)

            # Handle validation for when the validator returns a dictionary
            if type(validator_result) is dict:
                if not validator_result['valid']:
                    display = f'{validator_result["message"]} {display_string}'
                    continue

                return user_input

            # Handle validation for when the validator returns a boolean
            if not validator_result:
                display = f'[{error_msg}] {display_string}'
                continue

            return user_input
