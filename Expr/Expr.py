# -*- coding: utf-8 -*-
from MP_func.MP_Func import *

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        print(info(2))
    except Exception:
        print(info(1))

def main():
    while True:
        expr = input("|- expr mode -| >>> ")
        expr = expr.lower()
        expr = expr.split(':')
        if "exit" in expr:
            break
        elif "round" in expr:
            try:
                print(expr[1], '≈', round(float(expr[1]), int(expr[2])))
            except Exception:
                print(info(1))
        elif "help" in expr:
            try:
                if "-en" == expr[1]:
                    with open(f"{__file__}/help_Expr/help_Expr.dat", 'r') as help_en:
                        data = help_en.read()
                    print(data)
                elif "-zh" == expr[1]:
                    with open(f"{__file__}/help_Expr/help_Expr-zh.dat", 'r', encoding="utf-8") as help_zh:
                        data = help_zh.read()
                    print(data)
                elif "-fr" == expr[1]:
                    with open(f"{__file__}/help_Expr/help_Expr-fr.dat", 'r', encoding="utf-8") as help_fr:
                        data = help_fr.read()
                    print(data)
                elif "-jp" == expr[1]:
                    with open(f"{__file__}/help_Expr/help_Expr-jp.dat", 'r', encoding="utf-8") as help_jp:
                        data = help_jp.read()
                    print(data)
            except Exception:
                try:
                    with open(f"{__file__}/help_ help_Expr.dat", 'r') as help_en:
                        data = help_en.read()
                    print(data)
                except Exception:
                    print(info(5))
        else:
            result = calculate("".join(expr))
            print("".join(expr), '=', result)