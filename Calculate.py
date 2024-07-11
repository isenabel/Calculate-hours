from datetime import datetime

print("""Insert date & time (24 hour format) using the following format:
      
month/day/year hour:minute
00/00/0000 00:00

Example: 07/10/2024 23:59      
""")

# d1 = input('')

date1 = datetime.strptime('07/10/24 10:00',
                          '%m/%d/%y %H:%M')
date2 = datetime.strptime('07/11/24 11:00',
                          '%m/%d/%y %H:%M')

diference = date2 - date1
result = {
  "hours": (diference.days * 24) + (int(diference.seconds / 3600)),
  "minutes": (diference.seconds / 60) - ((int(diference.seconds / 3600)) * 60 )
}

print('%d hour/s and %d minute/s' % (result["hours"], result["minutes"]))