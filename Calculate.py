from datetime import datetime

print("""Insert date & time (24 hour format) using the following format:
      
month/day/year hour:minute
00/00/0000 00:00

Example: 07/10/2024 23:59

*Second date must be greater than the first date*
""")

def calDate(date1, date2):

  diference = date2 - date1
  result = {
    "hours": (diference.days * 24) + (int(diference.seconds / 3600)),
    "minutes": (diference.seconds / 60) - ((int(diference.seconds / 3600)) * 60 )
  }

  print('%d hour/s and %d minute/s' % (result["hours"], result["minutes"]))

while True:
  try:
    d1 = input('Insert first date: ')
    d2 = input('Insert second date: ')
        
    date1 = datetime.strptime(d1,'%m/%d/%Y %H:%M')
    date2 = datetime.strptime(d2,'%m/%d/%Y %H:%M')
        
    if ((date2.timestamp() - date1.timestamp()) < 0):
      raise Exception('First date greater than the second')
    else:
      calDate(date1, date2)
      break
  except Exception as err:
    print(f">>> Error: {err}")