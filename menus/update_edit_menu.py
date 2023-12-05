from utils import BaseMenu, Validator
from .edit_menu import IsbnEditMenu, AuthorTitleEditMenu


class UpdateMenu(BaseMenu):
    header = \
        '''
         _____    _ _ _     ____              _        
        | ____|__| (_) |_  | __ )  ___   ___ | | _____ 
        |  _| / _` | | __| |  _ \ / _ \ / _ \| |/ / __|
        | |__| (_| | | |_  | |_) | (_) | (_) |   <\__ \\
        |_____\__,_|_|\__| |____/ \___/ \___/|_|\_\___/                          
        '''

    def __init__(self, root):
        super().__init__(
            title='Update & Edit Books',
            header=self.header,
            root=root,
            sub_menus=[
                IsbnEditMenu(root=root),
                AuthorTitleEditMenu(root=root)
            ]
        )

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def list_update(self, index):
        # Display book that has been selected
        print()

        print('Here is information regarding the selected book:')
        print(str(self.root.book_list[index]))

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

        edit_type = int(Validator.input(
            display_string='Enter what you would like to change: ',
            validator=lambda x: x.isdigit() and int(x) in range(1, 9),
            error_msg='Must be within 1-8'
        ))

        print()

        # Change the information of the selected category
        if edit_type == 1:
            new_isbn = Validator.input(
                display_string='Enter the new International Standard Book Number (ISBN): ',
                validator=Validator.is_isbn
            )
            self.root.book_list[index].isbn = new_isbn

        elif edit_type == 2:
            first_name = Validator.input(
                display_string="Enter the Author's new First Name: ",
                validator=Validator.is_valid_string,
                error_msg='First Name should not consist a comma(s) or be empty'
            )
            surname = Validator.input(
                display_string="Enter the Author's new Surname: ",
                validator=Validator.is_valid_string,
                error_msg='Surname should not consist a comma(s) or be empty'
            )

            new_author = f"{first_name.title()} {surname.title()}"
            self.root.book_list[index].author = new_author

        elif edit_type == 3:
            new_title = Validator.input(
                display_string='Enter the new Title of the Book: ',
                validator=Validator.is_valid_string,
                error_msg='Title should not consist a comma(s) or be empty'
            ).title()
            self.root.book_list[index].title = new_title

        elif edit_type == 4:
            new_publisher = Validator.input(
                display_string='Enter the new Publisher: ',
                validator=Validator.is_valid_string,
                error_msg='Publisher should not consist a comma(s) or be empty'
            ).title()
            self.root.book_list[index].publisher = new_publisher

        elif edit_type == 5:
            new_genre = Validator.input(
                display_string='Enter the new Genre: ',
                validator=Validator.is_valid_string,
                error_msg='Genre should not consist a comma(s) or be empty'
            ).title()
            self.root.book_list[index].genre = new_genre

        elif edit_type == 6:
            new_year_published = Validator.input(
                display_string='Enter the new Year Published: ',
                validator=Validator.is_valid_year
            )
            self.root.book_list[index].year_published = new_year_published

        elif edit_type == 7:
            new_date_purchased = Validator.input(
                display_string='Enter the new Date Purchased: ',
                validator=Validator.is_valid_date
            )
            self.root.book_list[index].date_purchased = new_date_purchased

        elif edit_type == 8:
            new_status = Validator.input(
                display_string="Enter new Book Status ('to-read', 'reading', 'read'): ",
                validator=Validator.is_allowed_status,
                error_msg='Invalid Status'
            )
            self.root.book_list[index].status = new_status

        # Display Updated Information
        print()

        print('The information has been updated!')
        print(str(self.root.book_list[index]))

        print()

        # Allow user to edit another book or go back to main menu
        cont = Validator.input(
            display_string='Do you wish to delete another book (Y/N)?: ',
            validator=Validator.is_valid_confirmation
        ).upper()

        if cont == 'Y':
            self.display().selection()

        elif cont == 'N':
            self.root.display().selection()
