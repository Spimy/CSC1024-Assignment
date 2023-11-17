class InputHelper:
    def _contains_comma(self, string):
        '''
        Check if string contains a comma
        If a string contains a comma then splitting it with a comma should return
        an array with a length greater than 1  
        '''
        return len(string.split(',')) > 1
