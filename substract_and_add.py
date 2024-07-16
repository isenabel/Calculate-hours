"""Module providing a function to substract or add time"""

from datetime import timedelta

print(
    """Insert time (24 hour format) using the following format:
hour.minute.second
00.00.00

If you want to add or substract, put + or - symbol at the beginning.

You do not need to insert all 3 values.
You can insert only one or two values starting with the hours.

Examples: 
+01.00.00 (Add 1 hour)
+1 (Add 1 hour)
-0.10 (Substract 10 minutes) or -00.10.00
-0.0.10 (Substract 10 seconds)

Type "reset" to restart.
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
            print("")
            if time_input[0] == "+":
                aux = time_input[1:]
                splited_time = aux.split(".")
                time_list_len = len(splited_time)
                if time_list_len == 3:
                    time = timedelta(
                        hours=int(splited_time[0]),
                        minutes=int(splited_time[1]),
                        seconds=int(splited_time[2])
                    )
                elif time_list_len == 2:
                    time = timedelta(
                        hours=int(splited_time[0]),
                        minutes=int(splited_time[1])
                    )
                elif time_list_len == 1:
                    time = timedelta(
                        hours=int(splited_time[0])
                    )
                final_time += time
                print(final_time)

            elif time_input[0] == "-":
                aux = time_input[1:]
                splited_time = aux.split(".")
                time_list_len = len(splited_time)
                if time_list_len == 3:
                    time = timedelta(
                        hours=int(splited_time[0]),
                        minutes=int(splited_time[1]),
                        seconds=int(splited_time[2])
                    )
                elif time_list_len == 2:
                    time = timedelta(
                        hours=int(splited_time[0]),
                        minutes=int(splited_time[1])
                    )
                elif time_list_len == 1:
                    time = timedelta(
                        hours=int(splited_time[0])
                    )
                final_time -= time
                print(final_time)

            elif time_input == "quit" or time_input == "Quit":
                quit()
            elif time_input == "reset" or time_input == "Reset":
                time = timedelta()
                print(time)

        except ValueError:
            print("Error: Wrong format or value error")


init()
