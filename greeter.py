# Greeter is a terminal application that greets old friends warmly, and remembers new friends.
import pickle
import os
import re

def display_title_bar():
    """
    Displays the title of the greeter app.
    """
    print("\n", "\t************************************************")
    print("\t****  Greeter - Hello old and new friends!  ****")
    print("\t************************************************")
    print(f"\tThere are {len(names)} names that I have remembered so far!")

def enter_choice():
    """
    Prompts the user to enter a choice of action for the greeter app.
    """
    entered_choice = input("""
    Choose one of the following actions:

    [1] Enter a name
    [2] List all known names
    [3] Quit

    Choice: """)
    try:
        choice_as_int = int(entered_choice)
        if choice_as_int in (1, 2, 3):
            return choice_as_int
        else:
            print("\nPlease pick choices 1, 2, or 3.")
            return enter_choice()
    except:
        print("\nYou entered a string! Please pick choices 1, 2, or 3.")
        return enter_choice()

def load_names():
    """
    Loads saved names from pickle, or returns an empty set if there are no saved names.
    """
    try:
        with open("names.pydata", "rb") as file_object:
            names = pickle.load(file_object)
        return set(names)
    except:
        return set()

def request_name():
    """
    Prompts the user to enter a name.
    """
    entered_name = input("\nEnter a name: ")
    if re.match('^[a-zA-Z]+$|^[a-zA-Z]+ [a-zA-Z]+$', entered_name):
        return entered_name.title()
    else:
        print("\nYou entered a name with invalid characters! Please enter another name.")
        return request_name()

def quit():
    """
    Quits the greeter app and saves new names to pickle.
    """
    if names_init_len == len(names):
        print("\nThanks for playing! You did not add any new names.")
    else:
        try:
            with open("names.pydata", "wb") as file_object:
                pickle.dump(names, file_object)
            print("\nThanks for playing! I will remember all these names.")
        except:
            print("\nThanks for playing! I won't be able to remember all these names.")

if __name__ == '__main__':
    os.system('cls')

    names = load_names()
    names_init_len = len(names)

    display_title_bar()
    choice = enter_choice()

    while choice != 3:

        if choice == 1:
            capitalized_name = request_name()

            if capitalized_name in names:
                print(f"\nHello, {capitalized_name}, old friend.")
            else:
                print(f"\nIt's nice to meet you, {capitalized_name}. I will remember you.")
                names.add(capitalized_name)
        else:
            if len(names) == 0:
                print("\nThere are no known names yet!")
            else:
                print("")
                for name in names:
                    print(name)

        cont = input("\nContinue playing? (y/n): ")
        while cont not in ('y', 'n'):
            print("\nPlease enter either y or n!")
            cont = input("Continue playing? (y/n): ")
        if cont == 'y':
            os.system('cls')
            display_title_bar()
            choice = enter_choice()
        else:
            choice = 3

    else:
        quit()
