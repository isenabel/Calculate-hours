"""Module providing a function to calculate hours between 2 dates."""

from datetime import datetime
import sys


class BadDateOrder(Exception):
    """Exception for bad date order input

    Args:
      Exception (str): First date greater than the second
    """


print(
    """Insert date & time (24 hour format) using the following format:
      
month/day/year hour:minute
00/00/0000 00:00

Example: 07/10/2024 23:59

*Second date must be greater than the first date*
"""
)


def calculate_date(date1, date2):
    """Function to calculate the hours"""

    diference = date2 - date1
    result = {
        "hours": (diference.days * 24) + (int(diference.seconds / 3600)),
        "minutes": (diference.seconds / 60) - ((int(diference.seconds / 3600)) * 60),
    }

    print(f"{result['hours']} hour/s and {int(result['minutes'])} minute/s")

    while True:
        cont = input("Quit? (y/n): ")
        if cont in ("y", "Y", "yes", "Yes"):
            sys.exit(0)
        elif cont in ("n", "N", "no", "No"):
            main()
            break

def main():
    """The Main function"""

    while True:
        try:
            d1 = input("Insert first date: ")
            d2 = input("Insert second date: ")

            date1 = datetime.strptime(d1, "%m/%d/%Y %H:%M")
            date2 = datetime.strptime(d2, "%m/%d/%Y %H:%M")

            if (date2.timestamp() - date1.timestamp()) < 0:
                raise BadDateOrder("First date greater than the second")

            calculate_date(date1, date2)
            break

        except BadDateOrder as err:
            print(f"Error: {err}")

        except ValueError:
            print("Error: Wrong format")

main()
