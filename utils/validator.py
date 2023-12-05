from datetime import datetime


class Validator:
    def is_valid_string(self, string):
        '''
        Check if string is empty
        Check if string contains a comma
        If a string contains a comma then splitting it with a comma should return
        an array with a length greater than 1  
        '''
        return len(string) > 0 and len(string.split(',')) == 1

    def is_isbn(self, isbn):
        ''' 
        Check validity of string 
        Should not contain comma(s)
        Should not be an empty input
        Should be 10 or 13 digits long
        Should adhere to ISBN digit formatting
        If invalid print error message and return boolean False
        Ask user to type a valid isbn
        '''

        # Check for commas or empty input
        # Return a boolean
        if not self.is_valid_string(isbn):
            return {
                'valid': False,
                'message': "[ISBN should not contain a comma or be empty] "
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
            total = 0

            # Multiply first 9 digits by a decreasing number starting from 10
            for i in range(len(isbn) - 1):
                total = total + int(isbn[i]) * (10 - i)

            # Last character of an ISBN 10 Numbers can be an X
            # X is considered to have the value of 10
            if isbn[-1].upper() == 'X':
                total += 10
            else:
                total += int(isbn[-1])

            # Check for a remainder
            # If there is a remainder, isbn is invalid
            # Return boolean
            if total % 11 != 0:
                return {
                    'valid': False,
                    'message': "[Your 10 digit number is not an ISBN] "
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

            # Add both results of the total of the multiplications
            total = result1 + result2

            # Divide the total to obtain remainder and substract 10
            remainder = total % 10
            x = 10 - remainder if remainder != 0 else 0

            # If x equals to the last digit of the isbn then its valid
            # Return boolean
            if x != int(isbn[len(isbn) - 1]):
                return {
                    'valid': False,
                    'message': "[Your 13 digit number is not an ISBN] "
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
        return status.lower() in ('to-read', 'reading', 'read')

    def is_valid_confirmation(self, confirmation):
        return confirmation.lower() in ('y', 'n')

    def input(self, display_string, validator, error_msg=''):
        '''
        Prompt user for input and validate it before returning a value
        display_string - string to display when asking for user input
        validator - callback function to use to validate user input
        error_msg - optional parameter, the error message to display when validator returns a boolean
        '''
        display = display_string

        while True:
            user_input = input(display)
            validator_result = validator(user_input)

            # Handle validation for when the validator returns a dictionary
            if type(validator_result) is dict:
                if not validator_result['valid']:
                    display = f'{validator_result["message"]} {display_string}'
                    continue

                return user_input

            # Handle validation for when the validator returns a boolean
            if not validator_result:
                if error_msg != '':
                    display = f'[{error_msg}] {display_string}'
                else:
                    display = display_string
                continue

            return user_input
