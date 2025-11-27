import time, os
from menu_technical import basics, operators, program_intro, conditionals, loops, list_functions

# Greetings & Start
os.system('cls')
name = input("Enter your name: ")
start = input(f'Hello {name}, would you like to start the program? (y/n): ').lower()
os.system('cls')
if start == 'y':
    print("Program will start in: ")
    time.sleep(1)
    os.system('cls')
    for i in range(3, 0, -1):
        print(f'         {i}')
        time.sleep(1)
        os.system('cls')
elif start == 'n':
    print("Program will not start, bye...")
    exit()

# Introduction
intro = input("Would you like to see about the program? (y/n): ").lower()
if intro == 'y':
    os.system('cls')
    program_intro(name)
elif intro == 'n':
    os.system('cls')
    print("Skipping introduction...")

# Main Menu
while True:
    os.system('cls')
    print("========== MENU ==========")
    time.sleep(0.3)
    print("1. Basics")
    time.sleep(0.3) 
    print("2. Operators")
    time.sleep(0.3)
    print("3. Conditional Statements")
    time.sleep(0.3)
    print("4. Loops")
    time.sleep(0.3)
    print("5. List & Functions")
    time.sleep(0.3)
    print("6. Challenges")
    time.sleep(0.3)
    print("7. Extra Lesson")
    time.sleep(0.3)
    print("8. Practice Yourself")
    time.sleep(0.3)
    print("9. Guess The Output Game")
    print("0. Exit")
    time.sleep(0.3)
    print("==========================")
    time.sleep(0.3)

    pick = input("Select from the options above (0-9): ").lower()

    if pick == '1':
        basics(name)
    elif pick == '2':
        operators(name)
    elif pick == '3':
        conditionals(name)
    elif pick == '4':
        loops(name)
    elif pick == '5':
        list_functions()
    elif pick == '6':
        pass
    elif pick == '7':
        pass
    elif pick == '8':
        while True:
            os.system('cls')
            print("\n=================== PRACTICE YOURSELF ===================")
            print("Type Python code using the concepts you learned.")
            print("Type 'output' at the last line to run your code.")
            print("Type 'return' to go back to the menu.")
            print("\nNOTE:")
            print("- input(), import, exit(), quit() are NOT recommended.")
            print("  because it won't show the output properly")
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
                    print("This command is not allowed here. Please try again.")
                    continue

                if low_line == "output":
                    break

                user_lines.append(line)

            if user_lines:
                code = "\n".join(user_lines)
                print("\n============== OUTPUT ==============")
                try:
                    exec(code)
                    print("\nYour code is working!")
                except Exception as e:
                    print(f"There was an error in your code: {e}")
                print("====================================")

            again = input("\nTry another code? (y/n): ").lower()
            if again != 'y':
                os.system('cls')
                break

        os.system('cls')
    elif pick == '9':
        pass
    elif pick == '0':
        os.system('cls')
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
