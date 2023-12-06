from utils import Color


class DisplayHelper:
    '''
    Static helper class containing methods for displaying the list of books.
    This was done so that other menus can also display the books after performing their respective actions.
    '''

    @staticmethod
    def get_color_status(status):
        '''
        Takes the status column and returns it with appropriate colors based on its value.
        '''
        match(status.lower()):
            case 'to-read': return (f'{Color.RED}{status}{Color.ENDC}')
            case 'reading': return (f'{Color.YELLOW}{status}{Color.ENDC}')
            case 'read': return (f'{Color.GREEN}{status}{Color.ENDC}')
            case _: return status

    @staticmethod
    def display_table(flattened_book_list):
        '''
        Display the tabulated book details.
        '''
        headers = [
            'ISBN', 'Author', 'Title', 'Publisher',  'Genre', 'Year Published', 'Date Purchased', 'Status'
        ]

        # CALCULATIONS to find maximum length of each item in every column
        # Group headers and their respective datas(Asterisk to unpack data)
        column_widths = [
            max(len(str(item)) for item in column) for column in zip(headers, *flattened_book_list)
        ]

        # Group the headers and the calculated column widths
        # (^) to centre headers within respective column widths
        header_line = ' | '.join(
            f'{header:^{width}}' for header, width in zip(headers, column_widths)
        )

        print(header_line)
        print('-' * len(header_line))

        for row in flattened_book_list:

            # Create a list of formatted strings for each item in the row except the last one
            # This formatting is done for each string(isbn, author, title, etc...)
            # List will contain everything apart from Status column
            formatted_row = [
                f'{item:<{width}}' for item, width in zip(row[:-1], column_widths[:-1])
            ]

            # Calls the function to display the colours for status column
            status_colored = DisplayHelper.get_color_status(row[-1])

            # After adding colours, append every Status with the colours back into the columns
            formatted_row.append(f'{status_colored:<{column_widths[-1]}}')

            # Joins every string together as one with '|' as a seperator
            row_line = ' | '.join(formatted_row)
            print(row_line)

        print('-' * len(header_line))
