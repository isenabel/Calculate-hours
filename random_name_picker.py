"""Randomize the order of inserted values."""

import random
import sys

print("""Use "," to separate each name.
Example: Marcos, Pedro, Juan, Mateo
""")

def main():
    """The main function"""

    iterations: int = 0
    values = input("Insert values: ")
    new_list = [value.strip() for value in values.split(",")]
    print()
    print("1) Single randomizer", "2) Make partners randomizer.", sep='\n')
    while True:
        option = input("Select option: ")
        print()

        if option in {'1', '1)', 'one', 'One'}:
            while len(new_list):
                iterations += 1
                print(f"{iterations}- {new_list.pop(random.randrange(len(new_list)))}")

            print('-' * 20)
            break

        if option in {'2', '2)', 'two', 'Two'}:
            while len(new_list):
                if iterations % 2 == 0:
                    print(f"{new_list.pop(random.randrange(len(new_list)))}", end=" <==> ")
                else:
                    print(f"{new_list.pop(random.randrange(len(new_list)))}")

                iterations += 1

            print('-' * 20)
            break

main()

while True:
    restart = input("Restart? (Yes or No): ")

    if restart in {'Yes', 'yes', 'Y', 'y'}:
        main()

    if restart in {'No', 'no', 'N', 'n'}:
        sys.exit(0)
