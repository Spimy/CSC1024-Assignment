class Utils:

    @staticmethod
    def find_book_index(book_list, **kwargs):
        '''
        Find the index of a book based on the attribute passed through the kwargs parameter
        Returns -1 if no book is found
        '''

        num_match = 0

        # Check if the key and attributes match to return the correct index
        for index, book in enumerate(book_list):
            for key in kwargs.keys():
                # If attribute does not match value then skip the current key
                if getattr(book, key, '').lower() != kwargs[key].lower():
                    break

                # Make sure all attributes match the values from kwargs
                num_match += 1
                if num_match == len(kwargs.keys()):
                    return index

            num_match = 0

        return -1
