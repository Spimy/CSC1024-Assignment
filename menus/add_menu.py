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
        super().__init__(title='Add Books', header=self.header, root=root)

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def selection(self):
        '''
        Allow user to input all book details and add it to the list
        Check for errors and allow user to re-input details if needed
        '''

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

        # Allow user to input name of Author
        # For consistency prompt for first name first
        while True:
            first_name = input(
                f"{'[First Name should not consist a comma(s)] ' if self.error_flags['first_name'] else ''}Enter the Author's First Name: "
            )

            # Guard Clause - if first_name is valid then break
            # If not valid - set error_flag to true
            if not self.root.validator.contains_comma(first_name):
                break

            self.error_flags['first_name'] = True

        # For consistency prompt for surname second
        while True:
            surname = input(
                f"{'[Surname should not consist a comma(s)] ' if self.error_flags['surname'] else ''}Enter the Author's Surname: "
            )

            # Guard Clause - if surname is valid then break
            # If not valid - set error_flag to true
            if not self.root.validator.contains_comma(surname):
                break

            self.error_flags['surname'] = True

        # Allow user to input Title name
        while True:
            title = input(
                f"{'[Title should not consist a comma(s)] ' if self.error_flags['title'] else ''}Enter the Title of the Book: "
            )

            # Guard Clause - if title is valid then break
            # If not valid - set error_flag to true
            if not self.root.validator.contains_comma(title):
                break

            self.error_flags['title'] = True

        # Allow user to input Publisher
        while True:
            publisher = input(
                f"{'[Publisher should not consist a comma(s)] ' if self.error_flags['publisher'] else ''}Enter the Publisher: "
            )

            # Guard Clause - if publisher is valid then break
            # If not valid - set error_flag to true
            if not self.root.validator.contains_comma(publisher):
                break

            self.error_flags['publisher'] = True

        # Allow user to input Genre
        while True:
            genre = input(
                f"{'[Genre should not consist a comma(s)] ' if self.error_flags['genre'] else ''}Enter the Genre: "
            )

            # Guard Clause - if genre is valid then break
            # If not valid - set error_flag to true
            if not self.root.validator.contains_comma(genre):
                break

            self.error_flags['genre'] = True

        # Allow user to input Year Published
        while True:
            year_published = input(
                f"{self.error_flags['year_published']['message'] if not self.error_flags['year_published']['valid'] else ''}Enter the Year Published: "
            )

            # Function from validator.py should check validity of Year Published
            # Should not contain comma(s)
            # Function from validator.py should check validity of isbn
            self.error_flags['year_published'] = self.root.validator.is_valid_year(
                year_published)

            # If valid then no need to ask for inout again
            if self.error_flags['year_published']['valid']:
                break

        # Allow user to input Date Purchased
        while True:
            date_purchased = input(
                f"{self.error_flags['date_purchased']['message'] if not self.error_flags['date_purchased']['valid'] else ''}Enter the Date Purchased: "
            )

            # Function from validator.py should check validity of Date Purchased
            # Should not contain comma(s)
            # Function from validator.py should check validity of isbn
            self.error_flags['date_purchased'] = self.root.validator.is_valid_date(
                date_purchased)

            # If valid then no need to ask for inout again
            if self.error_flags['date_purchased']['valid']:
                if int(date_purchased[6:len(date_purchased)]) < int(year_published):
                    self.error_flags['date_purchased']['valid'] = False
                    self.error_flags['date_purchased']['message'] = '[Year purchased cannot be less than the year published] '
                    continue
                else:
                    break

        # Allow user to input whether they have read, are reading or still need to read the book
        while True:
            status = input(
                f"{'[Invalid Status] ' if self.error_flags['status'] else ''}Enter Book Status ('to-read', 'reading', 'read'): "
            )

            # Guard Clause - if status is allowed then break
            # If not allowed - set error_flag to true
            if self.root.validator.is_allowed_status(status):
                break

            self.error_flags['status'] = True

        # Capitalise first letters of some lettered attributes
        first_name = first_name[0].upper() + first_name[1:]
        surname = surname[0].upper() + surname[1:]
        title = title[0].upper() + title[1:]
        publisher = publisher[0].upper() + publisher[1:]
        genre = genre[0].upper() + genre[1:]

        # Create new book
        # Concatenate first_name and surname using f string
        book = Book(
            isbn, f"{first_name} {surname}", title, publisher, genre, year_published, date_purchased, status
        )
        self.root.book_list.append(book)

        # Reassure user that book has been added
        print("Book has successfully been added!")
        print()

        # Reset flags so error codes are not initially run
        self.error_flags = {
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

        # Allow user to add another book or go back to main menu
        while True:
            cont = input("Do you wish to add another book (Y/N)?: ")

            if cont.upper() == "Y":
                return self.selection()
            elif cont.upper() == "N":
                return self.root.display().selection()
