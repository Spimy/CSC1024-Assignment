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
                'message': "[ISBN is invalid! ISBN should not contain a comma] "
            }

        # ISBN can only be 10 or 13 digits long
        # Check if isbn is NOT equal to a valid 10 or 13 digit number
        # Return boolean False
        if len(isbn) != 10 and len(isbn) != 13:
            return {
                'valid': False,
                'message': "[ISBN is invalid! ISBN should only contain 10 or 13 digits] "
            }

        # Check if isbn is equal to 10
        # If true check validity of isbn and return boolean
        if len(isbn) == 10:
            sum = 0

            # Multiply first 9 digits by a decreasing number starting from 10
            for i in range(len(isbn) - 1):
                sum = sum + int(isbn[i]) * (10 - i)

            # Last character of an ISBN 10 Numbers can be an X
            # X is considered to have the value of 10
            if isbn[-1].lower() == 'X':
                sum += 10
            else:
                sum += int(isbn[-1])

            # Check for a remainder
            # If there is a remainder, isbn is invalid
            # Return boolean
            if sum % 11 != 0:
                return {
                    'valid': False,
                    'message': "[ISBN is invalid! Your 10 digit number is not an ISBN] "
                }

        # Check if isbn is equal to 13
        # If true check validity of isbn and return boolean
        else:

            # Consider the first 12 digits
            # Multiply each consecutive digit by 1
            # Multiply each second consecutive digit by 3
            result1 = 0
            result2 = 0

            for i in range(len(isbn) - 1):
                if i % 2 == 0:
                    result1 += int(isbn[i]) * 1
                else:
                    result2 += int(isbn[i]) * 3

            # Add both results of the sum of the multiplications
            sum = result1 + result2

            # Divide the sum to obtain remainder and substract 10
            remainder = sum % 10
            x = 10 - remainder if remainder != 0 else 0

            # If x equals to the last digit of the isbn then its valid
            # Return boolean
            if x != int(isbn[len(isbn) - 1]):
                return {
                    'valid': False,
                    'message': "[ISBN is invalid! Your 13 digit number is not an ISBN] "
                }

        return {
            'valid': True,
            'message': ''
        }

    def is_valid_date(self, date_string):
        '''
        Check if string is a valid date in the format: DD-MM-YYYY
        Date cannot be greater than current date
        '''
        try:
            date = datetime.strptime(date_string, '%d-%m-%Y')
        except ValueError:
            return {
                'valid': False,
                'message': '[Date should be in the format: DD-MM-YYYY] '
            }

        if date.date() > datetime.now().date():
            return {
                'valid': False,
                'message': '[Date cannot be greater than current date] '
            }

        return {
            'valid': True,
            'message': ''
        }

    def is_valid_year(self, year_string):
        '''
        Check if string is a valid year
        Year cannot be greater than current year
        '''
        try:
            date = datetime.strptime(year_string, '%Y')
        except ValueError:
            return {
                'valid': False,
                'message': '[Year should be in the format: YYYY] '
            }

        if date.year > datetime.now().year:
            return {
                'valid': False,
                'message': '[Year cannot be greater than current year] '
            }

        return {
            'valid': True,
            'message': ''
        }

    def is_allowed_status(self, status):
        status_list = ('to-read', 'reading', 'read')
        return status.lower() in status_list
