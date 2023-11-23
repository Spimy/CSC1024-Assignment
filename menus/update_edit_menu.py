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

    def __init__(self, root):
        super().__init__(title='Update & Edit Books', header=self.header, root=root)

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
            else: 
                continue

        # Prompt user for the ISBN or Author + Title 
        # ISBN
        if choice == 1: 
            while True:
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

        # Check the ISBN or Author + Title
        # System for the user to edit and update information 


        # To return to the main menu 
        input('Hit enter to go back to main menu...')
        self.root.display().selection()
