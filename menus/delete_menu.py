from sqlite3 import Cursor
from typing import Self
from utils import BaseMenu


class DeleteMenu(BaseMenu):
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
        super().__init__(title='Delete Books', header=self.header, root=root)

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def selection(self):
        for i in range(len(self.root.book_list)):
            print(f'[{i + 1}] Book: {self.root.book_list[i].title}')

        while True:
            isbn = input("Enter ISBN of book you wish to edit: ")
            list:[1, 2, 3, 4, 5, 6, 7]
            result = list.count()


            
            
    def delete_book(book_list, book_title):
        for book in range(len(book_list["Books"])):
         if book_title in book_list["Books"][book]["Book's Title"]:
            print("Are you sure you want delete this book?: ")
        identifier = input()
        identifiers = ['y','n']
        while identifier not in identifiers:
            print("Please answer with y or n")
            print("Are you sure you want to delete this book?: ")
            identifier = input()
        if identifier == 'y':
            book.list["Books"][book].pop(book)
            return f"{book.title} is deleted from books library"
        
        input('Hit enter to go back to main menu...')
        Self.root.display().selection()
