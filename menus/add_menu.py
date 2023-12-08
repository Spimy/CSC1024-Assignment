from utils import BaseMenu, Book, Validator


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

    def execute(self):
        '''
        Allow user to input all book details and add it to the list
        Check for errors and allow user to re-input details if needed
        '''

        while True:
            isbn = Validator.input(
                display_string='Enter the International Standard Book Number (ISBN): ',
                validator=lambda x: Validator.is_valid_isbn(x, self.root)
            ).replace('-', '').replace(' ', '').upper()
            first_name = Validator.input(
                display_string="Enter the Author's First Name: ",
                validator=Validator.is_valid_string,
                error_msg='First Name should not consist a comma(s) or be empty'
            )
            surname = Validator.input(
                display_string="Enter the Author's Surname: ",
                validator=Validator.is_valid_string,
                error_msg='Surname should not consist a comma(s) or be empty'
            )
            title = Validator.input(
                display_string='Enter the Title of the Book: ',
                validator=Validator.is_valid_string,
                error_msg='Title should not consist a comma(s) or be empty'
            )
            publisher = Validator.input(
                display_string='Enter the Publisher: ',
                validator=Validator.is_valid_string,
                error_msg='Publisher should not consist a comma(s) or be empty'
            )
            genre = Validator.input(
                display_string='Enter the Genre: ',
                validator=Validator.is_valid_string,
                error_msg='Genre should not consist a comma(s) or be empty'
            )
            year_published = Validator.input(
                display_string='Enter the Year Published: ',
                validator=Validator.is_valid_year
            )

            date_purchased = Validator.input(
                display_string='Enter the Date Purchased: ',
                validator=lambda x: 
                    Validator.is_valid_date_purchased(x, year_published)
            )

            status = Validator.input(
                display_string="Enter Book Status ('to-read', 'reading', 'read'): ",
                validator=Validator.is_allowed_status,
                error_msg='Invalid Status'
            )

            # Convert inputs to title casing
            author = f'{first_name} {surname}'.title()
            title = title.title()
            publisher = publisher.title()
            genre = genre.title()

            # Create new book
            book = Book(
                isbn, author, title, publisher, genre, year_published, date_purchased, status
            )
            self.root.book_list.append(book)

            # Reassure user that book has been added
            print('Book has successfully been added!')
            print()

            # Allow user to add another book or go back to main menu
            cont = Validator.input(
                display_string='Do you wish to add another book (Y/N)?: ',
                validator=Validator.is_valid_confirmation
            ).upper()

            if cont == 'Y':
                # Clear the console and display the header again
                self.display()

            elif cont == 'N':
                self.root.display().execute()
                break
