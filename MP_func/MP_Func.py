# -*- coding: utf-8 -*-
import os

MP_PATH = os.path.dirname(os.path.realpath(__file__ + "\\.."))


class Style:
    NORMAL = '\33[0m'
    BOLD = '\33[1m'
    ITALIC = '\33[3m'
    UNDERLINE = '\33[4m'


class Black:
    BLACK = '\33[30m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    CYAN = '\33[36m'
    WHITE = '\33[37m'

    BOLD_BLACK = '\33[1m\33[30m'
    BOLD_RED = '\33[1m\33[31m'
    BOLD_GREEN = '\33[1m\33[32m'
    BOLD_YELLOW = '\33[1m\33[33m'
    BOLD_BLUE = '\33[1m\33[34m'
    BOLD_VIOLET = '\33[1m\33[35m'
    BOLD_CYAN = '\33[1m\33[36m'
    BOLD_WHITE = '\33[1m\33[37m'

    ITALIC_BLACK = '\33[3m\33[30m'
    ITALIC_RED = '\33[3m\33[31m'
    ITALIC_GREEN = '\33[3m\33[32m'
    ITALIC_YELLOW = '\33[3m\33[33m'
    ITALIC_BLUE = '\33[3m\33[34m'
    ITALIC_VIOLET = '\33[3m\33[35m'
    ITALIC_CYAN = '\33[3m\33[36m'
    ITALIC_WHITE = '\33[3m\33[37m'

    UNDERLINE_BLACK = '\33[4m\33[30m'
    UNDERLINE_RED = '\33[4m\33[31m'
    UNDERLINE_GREEN = '\33[4m\33[32m'
    UNDERLINE_YELLOW = '\33[4m\33[33m'
    UNDERLINE_BLUE = '\33[4m\33[34m'
    UNDERLINE_VIOLET = '\33[4m\33[35m'
    UNDERLINE_CYAN = '\33[4m\33[36m'
    UNDERLINE_WHITE = '\33[4m\33[37m'


class Background:
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    CYAN = '\33[36m'


def info(index: int, name=None) -> str:
    infolist = [f'{Black.BOLD_RED}Error: Unable to recognize the inputs{Style.NORMAL}',
                f'{Black.BOLD_RED}Error: Unable to recognize the number entered{Style.NORMAL}',
                f'{Black.BOLD_RED}Error: Divisor cannot be 0{Style.NORMAL}',
                f'{Black.BOLD_RED}Error: Can\'t find "{name}"{Style.NORMAL}',
                f"{Black.BOLD_RED}Error: Directory already exists{Style.NORMAL}",
                f'{Black.BOLD_RED}Please change dir to "Wosto_2_MP" dir to read the help.{Style.NORMAL}',
                f'{Black.ITALIC_GREEN}Successfully executed.{Style.NORMAL}']
    return infolist[index]


def sure(do: object = 'pass') -> bool:
    while True:
        is_true = input('sure?(y/n) ')
        while True:
            if is_true == 'y':
                exec(do)
                return True
            elif is_true == 'n':
                return False
            else:
                print(info(0))
                sure(do)
