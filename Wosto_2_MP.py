# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 21:14:32 2022
@author: fangg
"""
# 尽量减少第三方库的使用
from MP_func.MP_Func import *
import Expr_APP.Expr as expr
from shutil import *
from psutil import *
from sys import *
import os

while True:
    inputstr = input(f"WostoMP # {os.getcwd()} $ ")
    inputstr = inputstr.lower()
    inputstr = inputstr.strip()
    inputs = inputstr.split(' ', 1)
    command = inputs[0]
    if len(inputs) != 1:
        args = tuple(inputs[1].split(' '))

    # 已更新 Python 3.12，对是否使用 match + case 仍旧未确定
    if 'expr' == command or 'math' == command:
        expr.main()
    elif 'type' == command:
        try:
            readfile = args[0]
            with open(readfile, 'r') as fileread:
                readata = fileread.read()
                print(readata)
        except FileNotFoundError:
            print(info(0, readfile))
        except Exception:
            print(info(0))
    elif 'rm' == command:
        try:
            rmdata = args[0]
            sure("remove(rmdata)")
        except FileNotFoundError:
            print(f'\33[31mError: Can\'t find "{rmdata}"{Style.NORMAL}')
        except Exception:
            print(info(0))
        else:
            print(info(6))
    elif 'rmdir' == command:
        try:
            deldir = args[0]
            sure('rmtree(deldir)')
        except FileNotFoundError:
            print(f'\33[31mError: Can\'t find "{deldir}"')
        except Exception:
            print(info(0))
        else:
            print(info(6))
    elif 'ls' == command or 'dir' == command:
        try:
            if '-a' == command:
                hasp = 2
            else:
                hasp = 1
            ls = os.listdir(inputs[hasp])
        except Exception:
            ls = os.listdir(os.getcwd())
        for list in range(len(ls)):
            if ls[list][0] == '.' and hasp == 1:
                continue
            print(Black.BOLD_BLUE + ls[list] + Style.NORMAL)
    elif 'pwd' == command:
        print(Black.BOLD_BLUE + os.getcwd() + Style.NORMAL)
    elif 'cp' == command:
        # 提醒：复制到的地点需要是目录或是文件，如是文件，会被替换为原文件。
        # 如果想复制到指定目录中，可以使用/分隔目录，比如path/one/dir,path/one/file.txt等。
        try:
            cpdata = args[0]
            path = args[1]
            copy2(cpdata, path)
        except FileNotFoundError:
            print(info(3, cpdata))
        except Exception:
            print(info(0))
        else:
            print(info(6))
    elif 'move' == command:
        # 提醒：移动到的地点需要是目录，如目标位置不存在，原文件将会被重命名为目标位置。
        # 如果您想复制到指定目录中，可以使用/分隔目录，比如path/one/dir,path/one/file.txt等。
        try:
            movedata = args[0]
            path = args[1]
            move(movedata, path)
        except FileNotFoundError:
            print(info(3, movedata))
        except Exception:
            print(info(0))
        else:
            print(info(6))
    elif 'rename' == command:
        try:
            renamedata = args[0]
            newname = args[1]
            os.rename(renamedata, newname)
        except FileNotFoundError:
            print(info(3, renamedata))
        except Exception:
            print(info(0))
        else:
            print('Successfully executed.')
    elif 'cd' == command or 'chdir' == command:
        try:
            cdata = args[0]
            os.chdir(cdata)
        except FileNotFoundError:
            print(info(3, cdata))
        except Exception:
            print(info(0))
    elif 'top' == command or 'tasklist' == command or 'ps' == command:
        processes = process_iter()
        print(f'________Name________{Black.BLUE}|{Style.NORMAL}_PID_{Black.BLUE}|'
              f'{Style.NORMAL}Memory Usage{Black.BLUE}|{Style.NORMAL}')
        for process in processes:
            if len(process.name()) > 20:
                print(process.name()[:17] + f"...{Black.BLUE}|{Style.NORMAL}", end='')
            else:
                print(process.name() + (20 - len(process.name())) * ' ' + f"{Black.BLUE}|{Style.NORMAL}", end='')
            print(str(process.pid) + (5 - len(str(process.pid))) * ' ' + f'{Black.BLUE}|{Style.NORMAL}', end='')
            print(str(round(process.memory_percent(), 2)) +
                    (10 - len(str(round(process.memory_percent(), 2)))) * ' ' + f' %{Black.BLUE}|{Style.NORMAL}')
    elif 'taskkill' == command:
        try:
            if '/pid' == command:
                hasp = 2
            else:
                hasp = 1
            processes = process_iter()
            for process in processes:
                if hasp == 2 and process.pid == inputs[hasp]:
                    sure('system("taskkill /f /pid " + str(process.pid) + " /t")')
                if process.name() == inputs[hasp]:
                    sure('system("taskkill /f /im " + process.name() + " /t")')
        except Exception:
            print(info(0))
    elif 'md' == command or 'mkdir' == command:
        try:
            dirname = args[0]
            os.mkdir(dirname)
        except FileExistsError:
            print(info(4))
        except Exception:
            print(info(0))
    elif 'exit' == command or 'quit' == command:
        exit(0)
    elif 'echo' == command:
        try:
            print(args[0])
        except Exception:
            print(info(0))
    elif 'help' == command:
        try:
            if "-en" == command:
                with open("help/help.dat", 'r') as help_en:
                    data = help_en.read()
                print(data)
            elif "-zh" == command:
                with open("help/help-zh.dat", 'r', encoding="utf-8") as help_zh:
                    data = help_zh.read()
                print(data)
            elif "-fr" == command:
                with open("help/help-fr.dat", 'r') as help_fr:
                    data = help_fr.read()
                print(data)
            elif "-jp" == command:
                with open("help/help-jp.dat", 'r', encoding="utf-8") as help_jp:
                    data = help_jp.read()
                print(data)
        except Exception:
            try:
                with open("help/help.dat", 'r') as help_en:
                    data = help_en.read()
                print(data)
            except Exception:
                print(info(5))
    else:
        try:
            if command + '.exe' in os.listdir("App"):
                os.popen(command + '.exe')
            elif command + '.bat' in os.listdir("App"):
                os.popen(command + '.bat')
            else:
                print(f'\33[31m"{command}" is neither a command or an applications.{Style.NORMAL}')
        except FileNotFoundError:
            print(f'{Black.BOLD_RED}"{command}" is neither a command or an applications.{Style.NORMAL}')
# 添加第三方软件的接口