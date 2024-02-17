# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 21:14:32 2022
@author: fangg
"""
from decimal import *
from os import *
from shutil import *

supmap = str.maketrans('1234567890', '¹²³⁴⁵⁶⁷⁸⁹⁰')
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

while True:
    inputstr = input("|- Wosto 2 MP -| >>> ")
    inputstr = inputstr.lower()
    inputstr = inputstr.strip()
    inputs = inputstr.split(' ')

    if 'expr' in inputs:
        while True:
            exprinputstr = input("|- expr mode -| >>> ")
            exprinputstr = exprinputstr.lower()
            exprinputstr = exprinputstr.strip()
            exprinput = exprinputstr.split(' ')
            if 'plus' in exprinput:
                try:                                                        # 没改好，懒得改
                    plusresult = Decimal(exprinput[1]) + Decimal(exprinput[2])
                    print(exprinput[1], '+', exprinput[2], '=', plusresult)
                except:
                    print('\33[31mError: Unable to recognize the number entered\33[0m')
            if 'mine' in exprinput:
                try:
                    mineresult = Decimal(exprinput[1]) + Decimal(exprinput[2])
                    print(exprinput[1], '-', exprinput[2], '=', mineresult)
                except:
                    print('\33[31mError: Unable to recognize the number entered\33[0m')
            if 'multipli' in exprinput:
                try:
                    multipliresult = Decimal(exprinput[1]) * Decimal(exprinput[2])
                    print(exprinput[1], '×', exprinput[2], '=', multipliresult)
                except:
                    print('\33[31mError: Unable to recognize the number entered\33[0m')
            if 'divi' in exprinput:
                try:
                    diviresult = Decimal(exprinput[1]) / Decimal(exprinput[2])
                    print(exprinput[1], '÷', exprinput[2], '=', diviresult)
                except ZeroDivisionError:
                    print('\33[31mError: Divisor cannot be 0\33[0m')
                except:
                    print('\33[31mError: Unable to recognize the number entered\33[0m')
            if 'intdivi' in exprinput:
                try:
                    intdivi_result = Decimal(exprinput[1]) // Decimal(exprinput[2])
                    print(exprinput[1], '//', exprinput[2], '=', intdivi_result)
                except ZeroDivisionError:
                    print('\33[31mError: Divisor cannot be 0\33[0m')
                except:
                    print('\33[31mError: Unable to recognize the number entered\33[0m')
            if 'remainder' in exprinput:
                try:
                    remainder_result = Decimal(exprinput[1]) % Decimal(exprinput[2])
                    print(exprinput[1], '%', exprinput[2], '=', remainder_result)
                except ZeroDivisionError:
                    print('\33[31mError: Divisor cannot be 0\33[0m')
                except:
                    print('\33[31mError: Unable to recognize the number entered\33[0m')
            if 'remainder' in exprinput:
                try:
                    remainder_result = Decimal(exprinput[1]) % Decimal(exprinput[2])
                    print(exprinput[1], '%', exprinput[2], '=', remainder_result)
                except ZeroDivisionError:
                    print('\33[31mError: Divisor cannot be 0\33[0m')
                except:
                    print('\33[31mError: Unable to recognize the number entered\33[0m')
            if 'power' or 'square' in exprinput:
                try:
                    if 'power' in exprinput:
                        poweresult = Decimal(exprinput[1]) ** Decimal(exprinput[2])
                        print(exprinput[1] + exprinput[2].translate(supmap), '=', poweresult)
                    else:
                        poweresult = Decimal(exprinput[1]) ** 2
                        print(exprinput[1] + '²', '=', poweresult)
                except:
                    print('\33[31mError: Unable to recognize the number entered\33[0m')
            if 'back' in exprinput or 'escape' in exprinput:
                break
    elif 'type' in inputs:
        try:
            readfile = inputs[1]
            with open(readfile, 'r') as fileread:
                readata = fileread.read()
                print(readata)
        except FileNotFoundError:
            print(f'\33[31mError: Can\'t find "{readfile}"\33[0m')
        except:
            print('\33[31mError: Unable to recognize the inputs\33[0m')
    elif 'rm' in inputs:
        try:
            rmdata = inputs[1]
            sure("remove(rmdata)")
        except FileNotFoundError:
            print(f'\33[31mError: Can\'t find "{rmdata}"')
        except:
            print('\33[31mError: Unable to recognize the inputs\33[0m')
        else:
            print('Successfully executed.')
    elif 'rmdir' in inputs:
        try:
            deldir = inputs[1]
            sure('rmtree(deldir)')
        except FileNotFoundError:
            print(f'\33[31mError: Can\'t find "{deldir}"')
        except:
            print('\33[31mError: Unable to recognize the inputs\33[0m')
        else:
            print('Successfully executed.')
    elif 'ls' in inputs or 'dir' in inputs:
        try:
            if '-a' in inputs:
                hasp = 2
            else:
                hasp = 1
            ls = listdir(inputs[hasp])
        except:
            ls = listdir(getcwd())
        for list in range(len(ls)):
            if ls[list][0] == '.' and hasp == 1:
                continue
            print("\33[34m" + ls[list] + "\33[0m")
    elif 'pwd' in inputs:
        print("\33[34m" + getcwd() + "\33[0m")
    elif 'cp' == inputs[0]:
        # 提醒：复制到的地点需要是目录或是文件，如是文件，被复制到的文件将会被替换为原文件。
        # 如果想复制到指定目录中，可以使用/分隔目录，比如path/one/dir,path/one/file.txt等。
        try:
            cpdata = inputs[1]
            path = inputs[2]
            copy2(cpdata, path)
        except FileNotFoundError:
            print(f'\33[31mError: Can\'t find "{cpdata}"')
        except:
            print('\33[31mError: Unable to recognize the inputs\33[0m')
        else:
            print('Successfully executed.')
    elif 'move' == inputs[0]:
        # 提醒：移动到的地点需要是目录，如目标位置不存在，原文件将会被重命名为目标位置。
        # 如果您想复制到指定目录中，可以使用/分隔目录，比如path/one/dir,path/one/file.txt等。
        try:
            movedata = inputs[1]
            path = inputs[2]
            move(movedata, path)
        except FileNotFoundError:
            print(f'\33[31mError: Can\'t find "{movedata}"')
        except:
            print('\33[31mError: Unable to recognize the inputs\33[0m')
        else:
            print('Successfully executed.')
    elif 'rename' == inputs[0]:
        try:
            renamedata = inputs[1]
            newname = inputs[2]
            rename(renamedata, newname)
        except FileNotFoundError:
            print(f'\33[31mError: Can\'t find "{renamedata}"')
        except:
            print('\33[31mError: Unable to recognize the inputs\33[0m')
        else:
            print('Successfully executed.')