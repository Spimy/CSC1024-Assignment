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
