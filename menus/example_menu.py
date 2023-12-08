from utils import BaseMenu


class ExampleMenu(BaseMenu):
    header = \
        '''
 _____                           _        __  __                  
| ____|_  ____ _ _ __ ___  _ __ | | ___  |  \/  | ___ _ __  _   _ 
|  _| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \ | |\/| |/ _ \ '_ \| | | |
| |___ >  < (_| | | | | | | |_) | |  __/ | |  | |  __/ | | | |_| |
|_____/_/\_\__,_|_| |_| |_| .__/|_|\___| |_|  |_|\___|_| |_|\__,_|
                          |_|                                     
        '''

    def __init__(self, root):
        super().__init__(title='Example Menu', header=self.header, root=root)

        # NOTE: This is done purely for intellisense to work
        # If you do not need intellisense anymore, this line should be removed
        self.root = root

    def execute(self):
        for i in range(len(self.root.book_list)):
            print(f'[{i + 1}] Book: {self.root.book_list[i].title}')

        input('Hit enter to go back to main menu...')
        self.root.display().execute()
