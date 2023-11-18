from datetime import datetime


class Validator:
    def contains_comma(self, string):
        '''
        Check if string contains a comma
        If a string contains a comma then splitting it with a comma should return
        an array with a length greater than 1  
        '''
        return len(string.split(',')) > 1

    def is_isbn(self, isbn):

        ''' 
        Check validity of string 
        Should not contain comma(s)
        Should be 10 or 13 digits long
        Should adhere to ISBN digit formatting
        If invalid print error message and return boolean False
        Ask user to type a valid isbn
        '''

        # Check for commas
        # Return a boolean
        if self.contains_comma(isbn):
            return {
                'valid': False, 
                'message' : "ISBN is invalid! ISBN should not contain a comma. Please try again!"
                }
        
        # ISBN can only be 10 or 13 digits long
        # Check if isbn is NOT equal to a valid 10 or 13 digit number
        # Return boolean False
        if len(isbn) != 10 or len(isbn) != 13:
            return {
                'valid': False, 
                'message' : "ISBN is invalid! ISBN should only contain 10 or 13 digits. Please try again!"
                }
        
        
        # Check if isbn is equal to 10
        # If true check validity of isbn and return boolean
        if len(isbn) == 10:
            sum = 0

            # Multiply first 9 digits by a decreasing number starting from 10
            for i in range (len(isbn)):
                sum = sum + isbn[i] * (10 - i)
            
            # Last character of an ISBN 10 Numbers can be an X
            # X is considered to have the value of 10
            if isbn[9].lower() == 'X':
                sum += 10
            else:
                sum += int(isbn[9])

            
            # Check for a remainder 
            # If there is a remainder, isbn is invalid
            # Return boolean
            if sum % 11 == 0:
               return {'valid': True,
                       'message': ''
                        }    
            else:
               return {
                    'valid': False, 
                    'message' : "ISBN is invalid! Your 10 digit number is not an ISBN. Please try again!"
                    } 
            
        
        # Check if isbn is equal to 13
        # If true check validity of isbn and return boolean
        if len(isbn) == 13:

            # Consider the first 12 digits
            # Multiply each consecutive digit by 1
            # Multiply each second consecutive digit by 3
            result1 = isbn[0] * 1 + isbn[2] * 1 + isbn[4] * 1 + isbn[6] * 1 + isbn[8] * 1 + isbn[10] * 1
            result2 = isbn[1] * 3 + isbn[3] * 3 + isbn[5] * 3 + isbn[7] * 3 + isbn[9] * 3 + isbn[11] * 3

            # Add both results of the sum of the multiplications
            sum = result1 + result2

            # Divide the sum to obtain remainder and substract 10
            x = 10 - (sum % 10)

            
            # If x equals to the last digit of the isbn then its valid
            # Return boolean
            if x == isbn[12]:
               return {'valid': True,
                       'message': ''
                        }    
            else:
                return {
                    'valid': False, 
                    'message' : "ISBN is invalid! Your 13 digit number is not an ISBN. Please try again!"
                    } 
    

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

    def is_valid_year(self, year_string):
        '''
        Check if string is a valid year
        Year cannot be greater than current year
        '''
        try:
            date = datetime.strptime(year_string, '%Y')
        except ValueError:
            return False

        if date.year > datetime.now().year:
            return False

        return True
