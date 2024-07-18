"""Randomize the order of inserted values."""

import random
import sys

print("""Use "," to separate each name.
      Example: Marcos, Pedro, Juan, Mateo
      """)

def main():
    """The main function
    """

    values = input("Insert values: ")
    no_space = values.replace(' ', '')
    new_list = no_space.split(",")
    iterations: int = 0

    while len(new_list):
        iterations += 1
        print(f"{iterations}- {new_list.pop(random.randrange(len(new_list)))}")

main()
print('-' * 10)

while True:
    restart = input("Restart? (Yes or No): ")

    if restart in ('Yes', 'yes', 'Y', 'y'):
        main()
        break
    if restart in ('No', 'no', 'N', 'n'):
        sys.exit(0)
