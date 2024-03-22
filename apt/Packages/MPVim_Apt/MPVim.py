# -*- coding: utf-8 -*-
"""
Create on Mon Mar 11 19:32:25 2024
@author: fangg
"""
import MP_func.MP_Func as func
import random

class MPVim:
    def __init__(self):
        self.lines = []
        self.is_saved = True
        self.current_line = 0
        self.insert_mode = False

    def start(self):
        with open("Welcome.dat", "r") as welcome:
            readlines = welcome.readlines()
            for line in range(6):
                print(readlines[line], end='')
            rand_num = random.randint(1, 3)
            print(readlines[5 + rand_num], end='')
            print(readlines[9], end='')
        while True:
            self.display()
            command = input(":").split()
            self.execute_command(command)

    def display(self):
        for i, line in enumerate(self.lines):
            prefix = ": " if i == self.current_line else "   "
            print(f"{prefix}{line}")

# TODO 需要添加更多功能
    def execute_command(self, command):
        if "i" in command:
            self.insert_mode = True
            self.insert_text()
        elif "w" in command:
            self.save_file()
        elif "q" in command:
            if self.is_saved:
                quit()
            else:
                print("No saved file!")
        elif "q!" in command:
            func.sure("quit()")
        elif "j" in command:
            self.move_cursor_down()
        elif "k" in command:
            self.move_cursor_up()
        elif "x" in command:
            self.save_file()
            quit()
        else:
            print(func.info(0))

    def insert_text(self):
        self.is_saved = False
        while True:
            line = input()
            if line == ".":
                self.insert_mode = False
                break
            self.lines.insert(self.current_line, line)
            self.current_line += 1

    def save_file(self):
        filename = input("Enter filename to save: ")
        with open(filename, "w") as f:
            f.write("\n".join(self.lines))

        print(func.info(6))

    def move_cursor_down(self):
        if self.current_line < len(self.lines) - 1:
            self.current_line += 1

    def move_cursor_up(self):
        if self.current_line > 0:
            self.current_line -= 1

if __name__ == '__main__':
    mp_vim = MPVim()
    mp_vim.start()