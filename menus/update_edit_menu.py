from utils import BaseMenu, Validator, DisplayHelper
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
                # This are in the sub menu edit_menu
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
        book = self.root.flatten_book_list()[index]
        DisplayHelper.display_table([book])

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
            book[edit_type - 1] = Validator.input(
                display_string='Enter the new International Standard Book Number (ISBN): ',
                validator=lambda x: Validator.is_valid_isbn(x, self.root)
            ).replace('-', '').replace(' ', '').upper()
            self.root.book_list[index].isbn = book[edit_type - 1]

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

            book[edit_type - 1] = f"{first_name.title()} {surname.title()}"
            self.root.book_list[index].author = book[edit_type - 1]

        elif edit_type == 3:
            book[edit_type - 1] = Validator.input(
                display_string='Enter the new Title of the Book: ',
                validator=Validator.is_valid_string,
                error_msg='Title should not consist a comma(s) or be empty'
            ).title()
            self.root.book_list[index].title = book[edit_type - 1]

        elif edit_type == 4:
            book[edit_type - 1] = Validator.input(
                display_string='Enter the new Publisher: ',
                validator=Validator.is_valid_string,
                error_msg='Publisher should not consist a comma(s) or be empty'
            ).title()
            self.root.book_list[index].publisher = book[edit_type - 1]

        elif edit_type == 5:
            book[edit_type - 1] = Validator.input(
                display_string='Enter the new Genre: ',
                validator=Validator.is_valid_string,
                error_msg='Genre should not consist a comma(s) or be empty'
            ).title()
            self.root.book_list[index].genre = book[edit_type - 1]

        elif edit_type == 6:
            book[edit_type - 1] = Validator.input(
                display_string='Enter the new Year Published: ',
                validator=Validator.is_valid_year
            )
            self.root.book_list[index].year_published = book[edit_type - 1]

        elif edit_type == 7:
            book[edit_type - 1] = Validator.input(
                display_string='Enter the new Date Purchased: ',
                validator=Validator.is_valid_date
            )
            self.root.book_list[index].date_purchased = book[edit_type - 1]

        elif edit_type == 8:
            book[edit_type - 1] = Validator.input(
                display_string="Enter new Book Status ('to-read', 'reading', 'read'): ",
                validator=Validator.is_allowed_status,
                error_msg='Invalid Status'
            )
            self.root.book_list[index].status = book[edit_type - 1]

        # Display Updated Information
        print()

        print('The information has been updated!')
        DisplayHelper.display_table([book])

        print()
