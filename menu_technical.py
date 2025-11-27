import time, os
from menu_lessons import prints, inputs, escape_sequences, length, evals 
from menu_lessons import arithmetic, assignment, comparison, logical, tries
from menu_lessons import if_elif_else, nested, combining
from menu_lessons import for_loops, while_loops, nested_loops, loop_control
from menu_lessons import lists, functions, importing_random, defs, dictionaries
from menu_lessons import challenge_1, challenge_2, challenge_3, challenge_4, challenge_5, challenge_6, challenge_7, challenge_8, challenge_9, challenge_10, challenge_11, challenge_12, challenge_13, challenge_14, challenge_15

# Introduction
def program_intro(name):
    print("================================= WELCOME =================================")
    time.sleep(0.3)
    print(f'Hello {name}, I\'m Teki. And welcome to Teki\'s Python Learning Program.')
    time.sleep(0.3)
    print("\nThis program is designed to help you learn Python step by step.")
    time.sleep(0.3)
    print("You will find lessons on basics, operators, conditional statements,")
    time.sleep(0.3)
    print("loops, data structures like lists and dictionaries, and small challenges.")
    time.sleep(0.3)
    print("You can even try coding yourself in the 'Try It Yourself' Section!")
    time.sleep(0.3)
    print("Plus there's extra lessons and challenges to test your skills.")
    time.sleep(0.3)
    print("\nEach lesson includes:")
    time.sleep(0.3)
    print("- Explanation in simple language")
    time.sleep(0.3)
    print("- Example inputs and outputs")
    time.sleep(0.3)
    print("- Try It Yourself section to practice coding")
    time.sleep(0.3)
    print("- Pause for you to absorb the information")
    time.sleep(0.3)
    print("\nYou can navigate the menus by entering the number of your choice.")
    time.sleep(0.3)
    print("Press 0 at any menu to go back or exit.")
    time.sleep(0.3)
    print("\nLet's get started!\n")
    time.sleep(0.3)
    input("Press Enter to continue: ")
    os.system('cls')

# Basics Options
def basics(name):
    while True:
        os.system('cls')
        print("\n========== BASICS ==========")
        time.sleep(0.3)
        print("1. Print Statements")
        time.sleep(0.3)
        print("2. Input & Variables")
        time.sleep(0.3)
        print("3. Escape Sequences")
        time.sleep(0.3)
        print("4. Length")
        time.sleep(0.3)
        print("5. Eval, Int, Str, Float, Type")
        time.sleep(0.3)
        print("0. Back to Main Menu")
        time.sleep(0.3)
        print("=============================")
        time.sleep(0.3)

        choice = input(f'Select an option {name} (0-5): ').lower()

        if choice == '1':
            os.system('cls')
            prints()
            tries()
        elif choice == '2':
            os.system('cls')
            inputs()
            tries()
        elif choice == '3':
            os.system('cls')
            escape_sequences()
            tries()
        elif choice == '4':
            os.system('cls')
            length()
            tries()
        elif choice == '5':
            os.system('cls')
            evals()
            tries()
        elif choice == '0':
            os.system('cls')
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice, try again.")
            continue

# Operators Options
def operators(name):
    while True:
        os.system('cls')
        print("\n========== OPERATORS ==========")
        time.sleep(0.3)
        print("1. Arithmetic Operators")
        time.sleep(0.3)
        print("2. Assignment Operators")
        time.sleep(0.3)
        print("3. Comparison Operators")
        time.sleep(0.3)
        print("4. Logical Operators")
        time.sleep(0.3)
        print("0. Back to Main Menu")
        time.sleep(0.3)
        print("================================")
        time.sleep(0.3)

        choice = input(f'Select an option {name} (0-4): ').lower()

        if choice == '1':
            os.system('cls')
            arithmetic()
            tries()
        elif choice == '2':
            os.system('cls')
            assignment()
            tries()
        elif choice == '3':
            os.system('cls')
            comparison()
            tries()
        elif choice == '4':
            os.system('cls')
            logical()
            tries()
        elif choice == '0':
            os.system('cls')
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice, try again.")
            continue

# Conditional Statements Options
def conditionals(name):
    while True:
        os.system('cls')
        print("\n====== CONDITIONAL STATEMENTS ======")
        time.sleep(0.3)
        print("1. If/Elif/Else Statements")
        time.sleep(0.3)
        print("2. Nested Conditions")
        time.sleep(0.3)
        print("3. Combining Conditions (and/or in if)")
        time.sleep(0.3)
        print("0. Back to Main Menu")
        time.sleep(0.3)
        print("=====================================")
        time.sleep(0.3)

        choice = input(f'Select an option {name} (0-3): ').lower()

        if choice == '1':
            os.system('cls')
            if_elif_else()
            tries()
        elif choice == '2':
            os.system('cls')
            nested()
            tries()
        elif choice == '3':
            os.system('cls')
            combining()
            tries()
        elif choice == '0':
            os.system('cls')
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice, try again.")
            continue

# Loops Options
def loops(name):
    while True:
        os.system('cls')
        print("\n========== LOOPS ==========")
        time.sleep(0.3)
        print("1. For Loops")
        time.sleep(0.3)
        print("2. While Loops")
        time.sleep(0.3)
        print("3. Nested Loops")
        time.sleep(0.3)
        print("4. Loop Control Statements")
        time.sleep(0.3)
        print("0. Back to Main Menu")
        time.sleep(0.3)
        print("=============================")
        time.sleep(0.3)

        choice = input(f'Select an option {name} (0-4): ').lower()

        if choice == '1':
            os.system('cls')
            for_loops()
            tries()
        elif choice == '2':
            os.system('cls')
            while_loops()
            tries()
        elif choice == '3':
            os.system('cls')
            nested_loops()
            tries()
        elif choice == '4':
            os.system('cls')
            loop_control()
            tries()
        elif choice == '0':
            os.system('cls')
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice, try again.")
            continue

# List & Functions Options
def list_functions(name):
    while True:
        os.system('cls')
        print("\n====== LIST & FUNCTIONS ======")
        time.sleep(0.3)
        print("1. Lists")
        time.sleep(0.3)
        print("2. Functions")
        time.sleep(0.3)
        print("3. Def or define ")
        time.sleep(0.3)
        print("4. Importing Random")
        time.sleep(0.3)
        print("5. Dictionaries")
        time.sleep(0.3)
        print("0. Back to Main Menu")
        time.sleep(0.3)
        print("================================")
        time.sleep(0.3)

        choice = input(f'Select an option {name} (0-5): ').lower()

        if choice == '1':
            os.system('cls')
            lists()
            tries()
        elif choice == '2':
            os.system('cls')
            functions()
            tries()
        elif choice == '3':
            os.system('cls')
            defs()
            tries()
        elif choice == '4':
            os.system('cls')
            importing_random
            tries()
        elif choice == '5':
            os.system('cls')
            dictionaries()
            tries()
        elif choice == '0':
            os.system('cls')
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice, try again.")
            continue

# Challenges Options
def challenges(name):
    while True:
        os.system('cls')
        print("\n========== CHALLENGES ==========")
        time.sleep(0.3)
        print("1. Diamond with Name")
        time.sleep(0.3)
        print("2. ATM Denomination")
        time.sleep(0.3)
        print("3. Student Discount Checker")
        time.sleep(0.3)
        print("4. Manga Recommender")
        time.sleep(0.3)
        print("5. Factorial Calculator")
        time.sleep(0.3)
        print("6. Odd Number Summation")
        time.sleep(0.3)
        print("7. Countdown Simulator")
        time.sleep(0.3)
        print("8. Multiplication Table")
        time.sleep(0.3)
        print("9. Parrot Simulator")
        time.sleep(0.3)
        print("10. Reversed Staircase")
        time.sleep(0.3)
        print("11. Triangle Pattern")
        time.sleep(0.3)
        print("12. Pyramid Number")
        time.sleep(0.3)
        print("13. Odd/Even Summation")
        time.sleep(0.3)
        print("14. Anime List Maker")
        time.sleep(0.3)
        print("15. Student Information System")
        time.sleep(0.3)
        print("0. Back to Main Menu")
        time.sleep(0.3)
        print("===============================")
        time.sleep(0.3)

        choice = input(f'Select a challenge {name} (0-15): ').lower()

        if choice == '1':
            os.system('cls')
            challenge_1()
        elif choice == '2':
            os.system('cls')
            challenge_2()
        elif choice == '3':
            os.system('cls')
            challenge_3()
        elif choice == '4':
            os.system('cls')
            challenge_4()
        elif choice == '5':
            os.system('cls')
            challenge_5()
        elif choice == '6':
            os.system('cls')
            challenge_6()
        elif choice == '7':
            os.system('cls')
            challenge_7()
        elif choice == '8':
            os.system('cls')
            challenge_8()
        elif choice == '9':
            os.system('cls')
            challenge_9()
        elif choice == '10':
            os.system('cls')
            challenge_10()
        elif choice == '11':
            os.system('cls')
            challenge_11()
        elif choice == '12':
            os.system('cls')
            challenge_12()
        elif choice == '13':
            os.system('cls')
            challenge_13()
        elif choice == '14':
            os.system('cls')
            challenge_14()
        elif choice == '15':
            os.system('cls')
            challenge_15()
        elif choice == '0':
            os.system('cls')
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice, try again.")
            time.sleep(0.7)
            continue