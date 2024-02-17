# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 21:14:32 2022
@author: fangg
"""
from decimal import *

supmap = str.maketrans('1234567890', '¹²³⁴⁵⁶⁷⁸⁹⁰')
def sure():
    while True:
        bool = input('sure?(y/n)')
        if bool == 'y':
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


