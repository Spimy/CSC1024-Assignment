class BaseMenu:
    # Whether or not this is the root (main) menu
    # Used to determine whether to display the exit option or not
    root = False

    # Title of the menu used to be displayed in top-level menu
    title = None

    # Can be used to display ASCII art at the top of the menu
    header = None

    # List containing all submenus
    # This list should contain only objects that inherit BaseMenu
    sub_menus = []

    def __init__(self, title, root=False, header='', sub_menus=[]):
        '''
        Initialise the base menu object with provided arguments
        Only the title argument is required
        '''

        self.root = root
        self.title = title
        self.header = header
        self.sub_menus = sub_menus
