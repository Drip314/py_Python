import math

calculations = []
runden = 2
actions = "Rechnen (j/n) || Historie löschen (l) || Historie ansehen (h) || Runden einstellen (r): "

def Calc():
    try:

        first_num = float(input("1. number: "))
        op = input("(+, -, *, /, **, %, sqrt) : ")
        #sqrt hinzufügen
        if op == "sqrt":
            second_num = ""
        else:
            second_num = float(input("2. number: "))

        result = 0

        if op == "+":
            result = first_num + second_num
            print(round(result,runden))
        elif op == "-":
            result = first_num - second_num
            print(round(result,runden))
        elif op == "*":
            result = first_num * second_num
            print(round(result,runden))
        elif op == "/":
            result = first_num / second_num
            print(round(result,runden))
        elif op == "**":
            result = first_num ** second_num
            print(round(result,runden))
        elif op == "%":
            result = first_num % second_num
            print(round(result,runden))
        elif op == "sqrt":
            result = math.sqrt(first_num)
            print(round(result,runden))
        else:
            print("invalid operator")

        temp = f"{first_num} {op} {second_num} = {result}"
        calculations_file.write(f"\n{temp}")
        calculations.append(temp)

    except ZeroDivisionError:
        print("Divided by Zero")
    except ValueError:
        print("invalid input")

weiter = True
while weiter:
    calculations_file = open("calculations.txt", "a+")
    ja_nein = input(actions).lower()

    if ja_nein in ["j", "ja", "yes", "y"]:
        Calc()

    elif ja_nein in ["n", "nein", "no"]:
        print("In dieser Session durchgeführte Berechnungen.")
        for calc in calculations:
            print(calc)
        weiter = False
        calculations_file.close()

    elif ja_nein in ["l", "löschen"]:
        calculations_file.close()
        calculations_file = open("calculations.txt", "w")
        calculations_file.write(" ") 

    elif ja_nein in ["h"]:
        calculations_file.close()
        calculations_file = open("calculations.txt", "r")
        print(calculations_file.read())

    elif ja_nein in ["r"]:
        runden = int(input("Runden auf Nachkommastelle: "))

    else:
        print("Ungültige Eingabe")
        weiter = False
        calculations_file.close()