import os
import time



def seperator():
    print("-" * 30)


def print_menu():

    # is there a way to clear the console
    seperator()
    print('Welcome to PyCalc')
    seperator()

    print('[1] - Add')
    print('[2] - Subtract')
    print('[3] - Multiply')
    print('[4] - Divide')
    print('[x] - Close')

    seperator()


def clear_screen():
    os.system("cls")


def sum(num1, num2):
    return num1 + num2


def Subtract(num1, num2):
    return num1 - num2


def Multiply(num1, num2):
    return num1 * num2


def Divide(num1, num2):

    if (num1, num2 == 0):
        return print('ZeroDivisionError: float division by zero')

    return num1 / num2
    time.sleep(3)
    clear_screen()


opc = ''
while (opc != 'x'):
    print_menu()
    opc = input('Please select an option: ')

    if (opc == 'x'):
        clear_screen()
        break  # break = finish loop

    num1 = float(input('First number: '))
    num2 = float(input('Second number: '))

    if (opc == '1'):
        clear_screen()
        print("Result: " + str(sum(num1, num2)))
        time.sleep(3)

    elif (opc == '2'):
        clear_screen()
        print("Result: " + str(Subtract(num1, num2)))
        time.sleep(3)

    elif (opc == '3'):
        clear_screen()
        print("Result: " + str(Multiply(num1, num2)))
        time.sleep(3)

    elif (opc == '4'):
        clear_screen()
        print("Result: " + str(Divide(num1, num2)))
        time.sleep(3)


input('Press Enter to continue...')

print('Byte Byte!')




# on div show error if the user tries to divide by 0]
# return 0 from the fn
