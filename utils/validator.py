from datetime import datetime


class Validator:
    def _contains_comma(self, string):
        '''
        Check if string contains a comma
        If a string contains a comma then splitting it with a comma should return
        an array with a length greater than 1  
        '''
        return len(string.split(',')) > 1

    def is_isbn(self, isbn):
        if self._contains_comma(isbn):
            return False

        if len(isbn) != 10 or len(isbn) != 13:
            return False

    def is_valid_date(self, date_string):
        '''
        Check if string is a valid date in the format: DD-MM-YYYY
        Date cannot be greater than current date
        '''
        try:
            date = datetime.strptime(date_string, '%d-%m-%Y')
        except ValueError:
            return False

        if date.date() > datetime.now().date():
            return False

        return True
