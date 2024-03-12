# -*- coding: utf-8 -*-
"""
Create on Mon Mar 11 19:32:25 2024
@author: fangg
"""
# FIXME 运行时会报错：Error in sitecustomize; set PYTHONVERBOSE for traceback
import MP_func.MP_Func as func
import random
is_saved = True

class MPVim:
    def __init__(self):
        self.lines = []
        self.current_line = 0
        self.insert_mode = False

    def run(self):
        with open("Welcome.dat", "r") as welcome:
            readlines = welcome.readlines()
            for line in range(6):
                print(readlines[line], end='')
            rand_num = random.randint(1, 3)
            print(readlines[5 + rand_num], end='')
            print(readlines[9], end='')
        while True:
            self.display()
            command = input(": ")
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
            if is_saved:
                quit()
            else:
                print("No saved file!")
        elif "q!" in command:
            func.sure("quit()")
        elif "j" in command:
            self.move_cursor_down()
        elif "k" in command:
            self.move_cursor_up()
        else:
            print(func.info(0))

    def insert_text(self):
        is_saved = False
        while True:
            line = input()
            if line == ".":
                self.insert_mode = False
                break
            self.lines.insert(self.current_line, line)
            self.current_line += 1

    def save_file(self):
        is_saved = True
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