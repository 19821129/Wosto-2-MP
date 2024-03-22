# -*- coding: utf-8 -*-
""""
Create on Fri Mar 15 17:33:07 2024
@author: fangg
"""
import os
import json
from typing import List, Any

import MP_func.MP_Func as func

os.chdir(func.MP_PATH)


class Apt:

    def __init__(self):
        self.apt_list = os.listdir(func.MP_PATH + "/apt/Packages")
        self.infolist = []
        for package in self.apt_list:
            with open(func.MP_PATH + "\\apt\\Packages\\" + package + '\\AptInfo.json', 'r',
                      encoding="utf-8") as apt_info:
                self.infolist.append(json.loads(apt_info.read()))

    def update(self) -> None:
        self.infolist.clear()
        for package in self.apt_list:
            with open(func.MP_PATH + "\\apt\\Packages\\" + package + '\\AptInfo.json', 'r',
                      encoding="utf-8") as update_info:
                self.infolist.append(json.loads(update_info.read()))

    def output_list(self) -> None:
        print(f"=======Package Name======={func.Black.BLUE}|{func.Style.NORMAL}"
              f"====Category===={func.Black.BLUE}|{func.Style.NORMAL}"
              f"=====Publisher====={func.Black.BLUE}|{func.Style.NORMAL}"
              f"===Version==={func.Black.BLUE}|{func.Style.NORMAL}"
              f"===Edition==={func.Black.BLUE}|{func.Style.NORMAL}")
        for info in range(len(self.infolist)):
            if len(self.infolist[info]['package_name']) > 26:
                print(self.infolist[info]['package_name'][:24] + f"...{func.Black.BLUE}|{func.Style.NORMAL}", end="")
            else:
                print(self.infolist[info]['package_name'] + (" " * (26 - len(self.infolist[info]['package_name']))) +
                      f'{func.Black.BLUE}|{func.Style.NORMAL}', end="")

            if len(self.infolist[info]['category']) > 16:
                print(self.infolist[info]['category'][:14] + f"...{func.Black.BLUE}|{func.Style.NORMAL}", end="")
            else:
                print(self.infolist[info]['category'] + (" " * (16 - len(self.infolist[info]['category']))) +
                      f'{func.Black.BLUE}|{func.Style.NORMAL}', end="")

            if len(self.infolist[info]['publisher']) > 19:
                print(self.infolist[info]['publisher'][:17] + f"...{func.Black.BLUE}|{func.Style.NORMAL}", end="")
            else:
                print(self.infolist[info]['publisher'] + (" " * (19 - len(self.infolist[info]['publisher']))) +
                      f'{func.Black.BLUE}|{func.Style.NORMAL}', end="")

            if len(self.infolist[info]['version']) > 13:
                print(self.infolist[info]['version'][:11] + f"...{func.Black.BLUE}|{func.Style.NORMAL}", end="")
            else:
                print(self.infolist[info]['version'] + (" " * (13 - len(self.infolist[info]['version']))) +
                      f'{func.Black.BLUE}|{func.Style.NORMAL}', end="")

            if len(self.infolist[info]['edition']) > 13:
                print(self.infolist[info]['edition'][:11] + f"...{func.Black.BLUE}|{func.Style.NORMAL}", end="")
            else:
                print(self.infolist[info]['edition'] + (" " * (13 - len(self.infolist[info]['edition']))) +
                      f'{func.Black.BLUE}|{func.Style.NORMAL}', end="")

apt_get = Apt()
apt_get.update()
apt_get.output_list()
print(apt_get.apt_list)
print(apt_get.infolist)
