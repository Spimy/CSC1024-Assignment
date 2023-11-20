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
        print("|  " + "  |  ".join(headers) + "  |")
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

        
    