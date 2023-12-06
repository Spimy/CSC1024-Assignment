class Book:
    '''
    Books from the text file should be loaded into a book object
    '''

    def __init__(self, isbn, author, title, publisher, genre, year_published, date_purchased, status):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.publisher = publisher
        self.genre = genre
        self.year_published = year_published
        self.date_purchased = date_purchased
        self.status = status

    @staticmethod
    def from_string(book_string):
        '''
        Convert book string from text files to a book object
        '''
        book = book_string.split(',')
        return Book(*book)

    def __iter__(self):
        return iter([self.isbn, self.author, self.title, self.publisher, self.genre, self.year_published, self.date_purchased, self.status])

    def __str__(self):
        return f'{self.isbn},{self.author},{self.title},{self.publisher},{self.genre},{self.year_published},{self.date_purchased},{self.status}'
