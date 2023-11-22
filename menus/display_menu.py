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
        headers = ["ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status"]
        data = []

        for i in range(len(self.root.book_list)):
            isbn = self.root.book_list[i].isbn
            author = self.root.book_list[i].author
            title = self.root.book_list[i].title
            publisher = self.root.book_list[i].publisher
            genre = self.root.book_list[i].genre
            year_published = self.root.book_list[i].year_published
            date_purchased = self.root.book_list[i].date_purchased
            status = self.root.book_list[i].status
            print()

            data.append([isbn, author, title, publisher, genre, year_published, date_purchased, status ])

        
        column_widths = [max(len(str(item)) for item in column) for column in zip(headers, *data)]

        header_line = " | ".join(f"{header:^{width}}" for header, width in zip(headers, column_widths))
        print(header_line)
        print("-" * len(header_line))

        for row in data:
            row_line = " | ".join(f"{item:<{width}}" for item, width in zip(row, column_widths))
            print(row_line)

        input("\nPress Enter to return to the main menu...")
        self.root.display().selection()

            
                