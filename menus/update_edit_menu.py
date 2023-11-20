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

        # Prompt user for the ISBN or Author + Title 
        # Check the ISBN or Author + Title 

        # System for the user to edit and update information 

        
        

        # To return to the main menu 
        input('Hit enter to go back to main menu...')
        self.root.display().selection()
