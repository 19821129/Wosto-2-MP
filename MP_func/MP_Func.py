# -*- coding: utf-8 -*-
class Style:
    NORMAL = '\33[0m'
    BOLD = '\33[1m'
    ITALIC = '\33[3m'
    UNDERLINE = '\33[4m'

class Black:
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE = '\33[36m'

class White:
    BLACK = '\33[40m'
    RED = '\33[41m'
    GREEN = '\33[42m'
    YELLOW = '\33[43m'
    BLUE = '\33[44m'
    VIOLET = '\33[45m'
    BEIGE = '\33[46m'

def errorText(type, name=None):
    if type == 0:
        return f'{Style.BOLD}{Black.RED}Error: Unable to recognize the inputs{Style.NORMAL}'
    elif type == 1:
        return f'{Style.BOLD}{Black.RED}Error: Unable to recognize the number entered{Style.NORMAL}'
    elif type == 2:
        return f'{Style.BOLD}{Black.RED}Error: Divisor cannot be 0{Style.NORMAL}'
    elif type == 3:
        return f'{Style.BOLD}{Black.RED}Error: Can\'t find "{name}"{Style.NORMAL}'
    elif type == 4:
        return f"{Style.BOLD}{Black.RED}Error: Directory already exists{Style.NORMAL}"
    elif type == 5:
        return f'{Style.BOLD}{Black.RED}Please change dir to "Wosto_2_MP" dir to read the help.{Style.NORMAL}'
    else:
        return 0

def sure(do='pass'):
    while True:
        bool = input('sure?(y/n)')
        if bool == 'y':
            exec(do)
            return True
        elif bool == 'n':
            return False
        else:
            print('\33[31mError: Unable to recognize the inputs\33[0m')
