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
        'isbn': False,
        'first_name': False,
        'surname': False,
        'title': False,
        'publisher': False,
        'genre': False,
        'year_published': False,
        'date_purchased': False,
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
        isbn = input("Enter the International Standard Book Number (ISBN): ")
        
        # User may input isbn with dashes or spaces
        # This should be removed before function is run
        isbn = isbn.replace("-", "").replace(" ", "").upper()

        # Function from validator.py should check validity of isbn
        isbn_validator = self.root.validator.is_isbn(isbn)

        # Error checking
        # Give user insight into why input is invalid
        # Return allowing user to try again
        if not isbn_validator['valid']:
            # Continuously ask user to reinput isbn if it is not valid
            print(isbn_validator['message'])
            return self.selection()
        
        
        # Allow user to input name of Author
        # For consistency prompt for first name first
        first_name = None

        while True:
            first_name = input(f"{'[First Name should not consist a comma(s)] ' if self.error_flags['first_name'] else ''}Enter the Author's First Name: ")
            
            # Guard Clause - if first_name is valid then break
            # If not valid - set error_flag to true
            if first_name is not None and not self.root.validator.contains_comma(first_name):
                break

            self.error_flags['first_name'] = True
    

        # For consistency prompt for surname second
        surname = input("Enter the Author's Surname: ")

        # Function from validator.py should check validity of surname
        # Should not contain comma(s)
        self.root.validator.contains_comma(surname)

        # Allow user to input Title name
        title = input("Enter the Title of the Book: ")

        # Function from validator.py should check validity of Title
        # Should not contain comma(s)
        self.root.validator.contains_comma(title)  

        # Allow user to input Publisher 
        publisher = input("Enter the Publisher: ")

        # Function from validator.py should check validity of Publisher
        # Should not contain comma(s)
        self.root.validator.contains_comma(publisher)   

        # Allow user to input Genre 
        genre = input("Enter the Genre: ")

        # Function from validator.py should check validity of Genre
        # Should not contain comma(s)
        self.root.validator.contains_comma(genre) 

        # Allow user to input Year Published
        year_published = input("Enter the Year Published: ")

        # Function from validator.py should check validity of Year Published
        # Should not contain comma(s)
        self.root.validator.is_valid_year(year_published) 

        # Allow user to input Date Purchased
        date_purchased = input("Enter the Date Purchased: ")

        # Function from validator.py should check validity of Date Purchased
        # Should not contain comma(s)
        self.root.validator.is_valid_date(date_purchased) 


        input('Hit enter to go back to main menu...')
        self.root.display().selection()
