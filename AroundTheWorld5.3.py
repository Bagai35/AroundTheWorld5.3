# ======================================================================================================================

def random():
    from random import randint
    import time
    print('эта игра "орёл и решка"')
    time.sleep(0.5)
    x='1'
    while x=='1':

        a=randint(1,2)
        if a==1:
            print('выпал орёл\n')
        if a==2:
            print('выпала решка\n')
            time.sleep(0.5)
        x=input('повторить скрипт?(да-1/нет-0):')
        if x=='0':
            print('скрипт прекращён')
            time.sleep(0.2)
            print('\n \n \n \n \n \n')
            main()

# ======================================================================================================================

def kvur():
    import math, time
    x = '1'
    while x == '1':
        a = int(input('a='))
        b = int(input('b='))
        c = int(input('c='))
        D = b ** 2 - 4 * a * c
        print('D={0}'.format(+D))

        if D < 0:
            print('коренй нет')
        elif D == 0:
            print('есть только один корень')
            x1 = (-b + math.sqrt(D)) / 2 * a
            print('x1={0}'.format(x1))
        else:
            print('есть два корня')
            x1 = (-b + math.sqrt(D)) / a * 2
            x2 = (-b - math.sqrt(D)) / a * 2
            print('x1={0}\nx2={1}'.format(x1, x2))

        x = input('повторить скрипт?(да-1/нет-0):')
        if x == '0':
            print('скрипт прекращён')
            time.sleep(0.2)
            print('\n \n \n \n \n \n')
            main()

# ======================================================================================================================

def cub():
    import time
    x = '1'
    while x == '1':
        a = int(input('введите длинну \n'))
        d = int(input('введите высоту \n'))
        for r in range(a):
            for v in range(d):
                print('*', end='')
            print()
        x = input('повторить скрипт?(да-1/нет-0):')
        if x == '0':
            print('скрипт прекращён')
            time.sleep(0.2)
            print('\n \n \n \n \n \n')
            main()

# ======================================================================================================================

def spammer():
    import pyautogui
    import time
    import pyperclip
    import keyboard
    a = '1'
    while a == '1':

        x = str(input('\nвведите слово, которым будет производится спам: \n'))
        y = int(input('сколько раз будет написанно слово: \n'))
        z = int(input('скорость вставки сообщений; \nминимальная задержка 0.1 (оптимально 1.0): \n'))
        print('у тебя есть 5 секунд что  бы войти в чат, в который будет проводится спам')
        time.sleep(5)
        print('спам начался')

        def spam(text: str, amount: int):

            pyperclip.copy(text)
            for _ in range(amount):
                time.sleep(z)
                keyboard.press_and_release('ctrl + v')
                pyautogui.press("enter")

        spam(x, y)
        time.sleep(1)
        a = input('повторить скрипт?(да-1/нет-0):')
        if a == '0':
            print('скрипт прекращён')
            time.sleep(0.2)
            print('\n \n \n \n \n \n')
            main()

# ======================================================================================================================

def main():
    import time, sys
    time.sleep(1)
    print('░█████╗░██████╗░░█████╗░██╗░░░██╗███╗░░██╗██████╗░  ████████╗██╗░░██╗███████╗\n'
          '██╔══██╗██╔══██╗██╔══██╗██║░░░██║████╗░██║██╔══██╗  ╚══██╔══╝██║░░██║██╔════╝\n'
          '███████║██████╔╝██║░░██║██║░░░██║██╔██╗██║██║░░██║  ░░░██║░░░███████║█████╗░░\n'
          '██╔══██║██╔══██╗██║░░██║██║░░░██║██║╚████║██║░░██║  ░░░██║░░░██╔══██║██╔══╝░░\n'
          '██║░░██║██║░░██║╚█████╔╝╚██████╔╝██║░╚███║██████╔╝  ░░░██║░░░██║░░██║███████╗\n'
          '╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝\n'
          '\n'
          '░██╗░░░░░░░██╗░█████╗░██████╗░██╗░░░░░██████╗░\n'
          '░██║░░██╗░░██║██╔══██╗██╔══██╗██║░░░░░██╔══██╗\n'
          '░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░░░░██║░░██║\n'
          '░░████╔═████║░██║░░██║██╔══██╗██║░░░░░██║░░██║\n'
          '░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║███████╗██████╔╝\n'
          '░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░   \n5.3')
    time.sleep(0.5)
    print('made by Bagai35')
    a = int(input('\nspam-1 cub-2 (ax2+bx+c=0)-3 flip coin-4 exit-0\n'))
    if a == 1:
        spammer()

    elif a == 2:
        cub()

    elif a == 3:
        kvur()

    elif a==4:
        random()

    elif a == 0:
        print('BB')
        time.sleep(1.5)
        sys.exit(0)

main()

# ======================================================================================================================
