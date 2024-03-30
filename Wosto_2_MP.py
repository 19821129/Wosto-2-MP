# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 21:14:32 2022
@author: fangg
"""
# TODO APT 添加进 Help 文件
# 尽量减少第三方库的使用
from MP_func.MP_Func import *
import Expr.Expr as expr
import apt.apt as apt
from shutil import *
from psutil import *
from sys import *
import os

while True:
    inputstr = input(f"WostoMP # {os.getcwd()} $ ")
    inputstr = inputstr.strip()
    inputs = inputstr.split(' ', 1)
    command = inputs[0].lower()
    if len(inputs) != 1:
        args = tuple(inputs[1].split(' '))

    if 'expr' == command or 'math' == command:
        expr.main()
    if 'type' == command or 'cat' == command:
        try:
            readfile = args[0]
            with open(readfile, 'r') as fileread:
                readata = fileread.read()
                print(readata)
        except FileNotFoundError:
            print(info(3, readfile))
        except Exception:
            print(info(0))
    elif 'rm' == command:
        try:
            rmdata = args[0]
            if sure():
                if os.path.isfile(rmdata):
                    os.remove(rmdata)
                else:
                    os.rmdir(rmdata)
        except FileNotFoundError:
            print(info(3, rmdata))
        except Exception:
            print(info(0))
        else:
            print(info(6))
    elif 'ls' == command or 'dir' == command:
        try:
            if '-a' in args:
                hasp = 1
            else:
                hasp = 0
            ls = os.listdir(args[hasp])
        except Exception:
            ls = os.listdir(os.getcwd())
        for list in range(len(ls)):
            if ls[list][0] == '.' and hasp == 1:
                continue
            print(Black.BOLD_BLUE + ls[list] + Style.NORMAL)
    elif 'pwd' == command:
        print(Black.BOLD_BLUE + os.getcwd() + Style.NORMAL)
    elif 'cp' == command:
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
    elif 'mv' == command:
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
            if args[0] == "~":
                args[0] = MP_PATH
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
            if '-pid' == args[0]:
                hasp = 1
            else:
                hasp = 0
            processes = process_iter()
            for process in processes:
                if hasp == 1 and process.pid == args[hasp]:
                    if sure():
                        process.kill()
                if process.name() == args[hasp]:
                    if sure():
                        process.kill()
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
    elif 'apt' == command:
        apt_get = apt.Apt()
        try:
            if args[0] == 'update':
                apt_get.update()
            elif args[0] == 'list':
                apt_get.output_list()
            elif args[0] == 'start':
                program_status = apt_get.start_program(args[1])
                if not program_status:
                    print(info(0))
        except:
            print(info(0))
    elif 'help' == command:
        try:
            if "-en" == args[0]:
                with open(f"{MP_PATH}\\help\\help.dat", 'r') as help_en:
                    data = help_en.read()
                print(data)
            elif "-zh" == args[0]:
                with open(f"{MP_PATH}\\help\\help-zh.dat", 'r', encoding="utf-8") as help_zh:
                    data = help_zh.read()
                print(data)
            elif "-fr" == args[0]:
                with open(f"{MP_PATH}\\help\\help-fr.dat", 'r', encoding="utf-8") as help_fr:
                    data = help_fr.read()
                print(data)
            elif "-jp" == args[0]:
                with open(f"{MP_PATH}\\help\\help-jp.dat", 'r', encoding="utf-8") as help_jp:
                    data = help_jp.read()
                print(data)
        except Exception:
            try:
                with open(f"{MP_PATH}\\help\\help.dat", 'r') as help_en:
                    data = help_en.read()
                print(data)
            except Exception:
                print(info(0))
    else:
        try:
            if command + '.exe' in os.listdir("App"):
                os.system(command + '.exe')
            elif command + '.bat' in os.listdir("App"):
                os.system(command + '.bat')
            else:
                print(f'{Black.BOLD_RED}"{command}" is neither a command or an applications.{Style.NORMAL}')
        except FileNotFoundError:
            print(f'{Black.BOLD_RED}"{command}" is neither a command or an applications.{Style.NORMAL}')
