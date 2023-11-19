from utils import BaseMenu


class AddMenu(BaseMenu):
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
        'year_published': {'valid': False,
                           'message': ''
        },
        'date_purchased': {'valid': False,
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
            isbn = input(f"[{self.error_flags['isbn']['message'] if not self.error_flags['isbn']['valid'] else ''}] Enter the International Standard Book Number (ISBN): ")
            
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
            first_name = input(f"{'[First Name should not consist a comma(s)] ' if self.error_flags['first_name'] else ''}Enter the Author's First Name: ")
            
            # Guard Clause - if first_name is valid then break
            # If not valid - set error_flag to true
            if not self.root.validator.contains_comma(first_name):
                break

            self.error_flags['first_name'] = True
    
    
        # For consistency prompt for surname second
        while True:
            surname = input(f"{'[Surname should not consist a comma(s)] ' if self.error_flags['surname'] else ''}Enter the Author's Surname: ")
            
            # Guard Clause - if surname is valid then break
            # If not valid - set error_flag to true
            if not self.root.validator.contains_comma(surname):
                break

            self.error_flags['surname'] = True


        # Allow user to input Title name
        while True:
            title = input(f"{'[Title should not consist a comma(s)] ' if self.error_flags['title'] else ''}Enter the Title of the Book: ")
            
            # Guard Clause - if title is valid then break
            # If not valid - set error_flag to true
            if not self.root.validator.contains_comma(title):
                break

            self.error_flags['title'] = True
    


        # Allow user to input Publisher 
        while True:
            publisher = input(f"{'[Publisher should not consist a comma(s)] ' if self.error_flags['publisher'] else ''}Enter the Publisher: ")
            
            # Guard Clause - if publisher is valid then break
            # If not valid - set error_flag to true
            if not self.root.validator.contains_comma(publisher):
                break

            self.error_flags['publisher'] = True


        # Allow user to input Genre 
        genre = input("Enter the Genre: ")
        while True:
            genre = input(f"{'[Genre should not consist a comma(s)] ' if self.error_flags['genre'] else ''}Enter the Genre: ")
            
            # Guard Clause - if genre is valid then break
            # If not valid - set error_flag to true
            if not self.root.validator.contains_comma(genre):
                break

            self.error_flags['genre'] = True

        # Allow user to input Year Published
        while True:
            year_published = input(f"[{self.error_flags['year_published']['message'] if not self.error_flags['year_published']['valid'] else ''}]Enter the Year Published: ")

            # Function from validator.py should check validity of Year Published
            # Should not contain comma(s)
            # Function from validator.py should check validity of isbn
            self.error_flags['year_published'] = self.root.validator.is_valid_year(year_published)
            
            # If valid then no need to ask for inout again
            if self.error_flags['year_published']['valid']:
                break

        # Allow user to input Date Purchased
        while True:
            date_purchased = input(f"[{self.error_flags['date_purchased']['message'] if not self.error_flags['date_purchased']['valid'] else ''}]Enter the Date Purchased: ")

            # Function from validator.py should check validity of Date Purchased
            # Should not contain comma(s)
            # Function from validator.py should check validity of isbn
            self.error_flags['date_purchased'] = self.root.validator.is_valid_date(date_purchased) 
            
            # If valid then no need to ask for inout again
            if self.error_flags['date_purchased']['valid']:
                break

            input('Hit enter to go back to main menu...')
            self.root.display().selection()
        
        # Allow user to input whether they have read, are reading or still need to read the book
        while True:
            status = input(f"{'[Invalid Status] ' if self.error_flags['status'] else ''}Enter Book Status ('to-read', 'reading', 'read'): ")
       
            # Guard Clause - if status is valid then break
            # If not valid - set error_flag to true
            if not self.root.validator.is_allowed_status(status):
                break

            self.error_flags['status'] = True


