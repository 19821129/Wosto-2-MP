# -*- coding: utf-8 -*-
""""
Create on Fri Mar 15 17:33:07 2024
@author: fangg
"""
import os
import json

import MP_func.MP_Func as func


class Apt:

    def __init__(self):
        self.apt_list = os.listdir(func.MP_PATH + "/apt/Packages")
        self.info_list = []
        for package in self.apt_list:
            with open(func.MP_PATH + "\\apt\\Packages\\" + package + '\\AptInfo.json', 'r',
                      encoding="utf-8") as apt_info:
                self.info_list.append(json.loads(apt_info.read()))

    def update(self) -> None:
        self.info_list.clear()
        for package in self.apt_list:
            with open(func.MP_PATH + "\\apt\\Packages\\" + package + '\\AptInfo.json', 'r',
                      encoding="utf-8") as update_info:
                self.info_list.append(json.loads(update_info.read()))

    def output_list(self) -> None:
        print(f"=======Package Name======={func.Black.BLUE}|{func.Style.NORMAL}"
              f"====Category===={func.Black.BLUE}|{func.Style.NORMAL}"
              f"=====Publisher====={func.Black.BLUE}|{func.Style.NORMAL}"
              f"===Version==={func.Black.BLUE}|{func.Style.NORMAL}"
              f"===Edition==={func.Black.BLUE}|{func.Style.NORMAL}")
        for info in range(len(self.info_list)):
            if len(self.info_list[info]['package_name']) > 26:
                print(self.info_list[info]['package_name'][:23] + f"...{func.Black.BLUE}|{func.Style.NORMAL}", end="")
            else:
                print(self.info_list[info]['package_name'] + (" " * (26 - len(self.info_list[info]['package_name']))) +
                      f'{func.Black.BLUE}|{func.Style.NORMAL}', end="")

            if len(self.info_list[info]['category']) > 16:
                print(self.info_list[info]['category'][:13] + f"...{func.Black.BLUE}|{func.Style.NORMAL}", end="")
            else:
                print(self.info_list[info]['category'] + (" " * (16 - len(self.info_list[info]['category']))) +
                      f'{func.Black.BLUE}|{func.Style.NORMAL}', end="")

            if len(self.info_list[info]['publisher']) > 19:
                print(self.info_list[info]['publisher'][:16] + f"...{func.Black.BLUE}|{func.Style.NORMAL}", end="")
            else:
                print(self.info_list[info]['publisher'] + (" " * (19 - len(self.info_list[info]['publisher']))) +
                      f'{func.Black.BLUE}|{func.Style.NORMAL}', end="")

            if len(self.info_list[info]['version']) > 13:
                print(self.info_list[info]['version'][:10] + f"...{func.Black.BLUE}|{func.Style.NORMAL}", end="")
            else:
                print(self.info_list[info]['version'] + (" " * (13 - len(self.info_list[info]['version']))) +
                      f'{func.Black.BLUE}|{func.Style.NORMAL}', end="")

            if len(self.info_list[info]['edition']) > 13:
                print(self.info_list[info]['edition'][:10] + f"...{func.Black.BLUE}|{func.Style.NORMAL}")
            else:
                print(self.info_list[info]['edition'] + (" " * (13 - len(self.info_list[info]['edition']))) +
                      f'{func.Black.BLUE}|{func.Style.NORMAL}')
    def start_program(self, programs_name: str) -> bool:
        if programs_name + "_Apt" in self.apt_list:
            os.system("python " + os.path.dirname(__file__) + "\\Packages\\" +
                      programs_name + "_Apt\\" + programs_name + ".py")
            return True
        else:
            return False