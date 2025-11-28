import time, os
from menu_technical import *

# Greetings & Start
os.system('cls')
name = input(green("Enter your name: "))
start = input(magenta(f'Hello {name}, would you like to start the program? {yellow('(y/n)'):} ')).lower()
os.system('cls')
if start == 'y':
    print(yellow("Program will start in: "))
    time.sleep(1)
    os.system('cls')
    for i in range(3, 0, -1):
        print(cyan(f'         {i}'))
        time.sleep(1)
        os.system('cls')
elif start == 'n':
    print("Program will not start, bye...")
    exit()

# Introduction
intro = input(green(f"Would you like to see introduction of the program? {yellow('y/n:')} ")).lower()
if intro == 'y':
    os.system('cls')
    program_intro(name)
elif intro == 'n':
    os.system('cls')
    print("Skipping introduction...")

# Main Menu
while True:
    os.system('cls')
    print("==========", bold(green("MENU")), ("=========="))
    time.sleep(0.1)
    print(f"{red('1')}. Basics")
    time.sleep(0.1) 
    print(f"{red('2')}. Operators")
    time.sleep(0.1)
    print(f"{red('3')}. Conditional Statements")
    time.sleep(0.1)
    print(f"{red('4')}. Loops")
    time.sleep(0.1)
    print(f"{red('5')}. List & Functions")
    time.sleep(0.1)
    print(f"{red('6')}. Challenges")
    time.sleep(0.1)
    print(f"{red('7')}. Extra Lesson")
    time.sleep(0.1)
    print(f"{red('8')}. Practice Yourself")
    time.sleep(0.1)
    print(f"{red('9')}. Guess The Output Game")
    time.sleep(0.1)
    print(f"{red('0')}. Exit")
    time.sleep(0.1)
    print("==========================")
    time.sleep(0.1)

    pick = input(green("Select from the options above (0-9): ")).lower()

    if pick == '1':
        basics(name)
    elif pick == '2':
        operators(name)
    elif pick == '3':
        conditionals(name)
    elif pick == '4':
        loops(name)
    elif pick == '5':
        list_functions(name)
    elif pick == '6':
        challenges(name)
    elif pick == '7':
        extras(name)
    elif pick == '8':
        while True:
            os.system('cls')
            print(f"\n=================== {bold(red('PRACTICE YOURSELF'))} ===================")
            time.sleep(0.3)
            print("Type Python code using the concepts you learned.")
            time.sleep(0.3)
            print("Type 'output' at the last line to run your code.")
            time.sleep(0.3)
            print("Type 'return' to go back to the menu.")
            time.sleep(0.3)
            print("\nNOTE:")
            time.sleep(0.3)
            print("- input(), import, exit(), quit() are NOT recommended.")
            time.sleep(0.3)
            print("  because it won't show the output properly")
            time.sleep(0.3)
            print("==========================================================\n")

            user_lines = []
            forbidden = ["input(", "import ", "exit(", "quit("]

            while True:
                line = input("> ")
                low_line = line.replace(" ", "").lower()

                if low_line == "return":
                    os.system('cls')
                    break

                if any(f in low_line for f in forbidden):
                    print(red("This command is not allowed here. Please try again."))
                    continue

                if low_line == "output":
                    break

                user_lines.append(line)

            if user_lines:
                code = "\n".join(user_lines)
                print("\n=============="), (green("OUTPUT")), ("==============")
                try:
                    exec(code)
                    print(green("\nYour code is working!"))
                except Exception as e:
                    print(red(f"There was an error in your code: {e}"))
                print(cyan("===================================="))

            again = input(green("\nTry another code? (y/n): ")).lower()
            if again != 'y':
                os.system('cls')
                break

        os.system('cls')
    elif pick == '9':
        guess(name)
    elif pick == '0':
        os.system('cls')
        print(green("Goodbye!"))
        break
    else:
        print(red("Invalid choice, try again."))
