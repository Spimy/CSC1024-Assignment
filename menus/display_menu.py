from utils import BaseMenu


class DisplayMenu(BaseMenu):
    header = \
        '''
__________               __     .____    ._____.                               
\______   \ ____   ____ |  | __ |    |   |__\_ |______________ _______ ___.__. 
 |    |  _//  _ \ /  _ \|  |/ / |    |   |  || __ \_  __ \__  \\_  __ <   |  | 
 |    |   (  <_> |  <_> )    <  |    |___|  || \_\ \  | \// __ \|  | \/\___  | 
 |______  /\____/ \____/|__|_ \ |_______ \__||___  /__|  (____  /__|   / ____| 
        \/                   \/         \/       \/           \/       \/                                  
       
         '''

    def __init__(self, root):
        super().__init__(title='Display Books', header=self.header, root=root)

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def selection(self):
        print("|  ISBN  |  Author  |  Title  |   Publisher  |  Genre  |  Year Published  |  Date Purchased  |  Status  |")
        book_list = []
        for idx, i in enumerate(range(1, len(self.root.book_list))):
            isbn = self.root.book_list[i].isbn
            title = self.root.book_list[i].title
            author = self.root.book_list[i].author
            publisher = self.root.book_list[i].publisher
            genre = self.root.book_list[i].genre
            year = self.root.book_list[i].year_published
            date = self.root.book_list[i].date_purchased
            status = self.root.book_list[i].status
            print(f"  {isbn}  |  {author}  |  {title}  |  {publisher}  |  {genre}  |  {year}  |  {date}  |  {status}  |")
            print()

        
    # [isbn1, title1, ..., isbn2, title2]
        


# class BookDisplay:
#     def __init__(self):
#         self.book_file = 'books_23020043.txt'

#     def display_book(self):
#         try:
#             with open(self.book_f, 'r') as file:
#                 lines = file.readlines()
#                 for i, line in enumerate(lines, start = 1):
#                     print(f"{i}. {line.strip()}")
#         except FileNotFoundError:
#             print('File Not Found!')
#         except Exception as e:
#             print("An error has occurred")

#         input('Hit enter to go back to main menu...')
#         self.root.display().selection()

# class search_book:
#     def search_by_isbn(self, isbn):
#         results = [book for book in self.books if book.isbn == isbn]
#         return results

#     def search_by_author(self, author):
#         results = [book for book in self.books if book.author == author]
#         return results

#     def search_by_title(self, title):
#         results = [book for book in self.books if book.title == title]
#         return results

# if __name__ == "__main__":
#     display = BookDisplay()
#     display.display_book()
#     search_term = input("Search for books by [ISBN, Title, or Author]:  ")
#     display2 = search_book()
#     display2.search_book(search_term)










