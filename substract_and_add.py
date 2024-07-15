"""Module providing a function to substract or add time"""

from datetime import timedelta

print(
    """Insert time (24 hour format) using the following format:
hour:minute:second
00:00:00

If you want to add or substract, put + or - symbol at the beginning.

Example: +12:10:00 or -7:7:7
"""
)

def init():
    """The initial function"""

    final_time = timedelta()
    while True:
        try:
            time_input = input(
                'Insert time with the operation number at first (type "quit" to exit): '
            )
            print('')
            if time_input[0] == "+":
                aux = time_input[1:]
                splited_time = aux.split(':')
                time1 = timedelta(hours=int(splited_time[0]), minutes=int(splited_time[1]), seconds=int(splited_time[2]))
                final_time += time1
                print(final_time)

            elif time_input[0] == "-":
                aux = time_input[1:]
                splited_time = aux.split(':')
                time1 = timedelta(hours=int(splited_time[0]), minutes=int(splited_time[1]), seconds=int(splited_time[2]))
                final_time -= time1
                print(final_time)

            elif time_input == "quit":
                quit()

        except ValueError:
            print("Error: Wrong format")


init()
