from datetime import datetime, timezone
from pytz import timezone

format="%H:%M  %m-%d-%y"

opened=datetime.strptime('09:00','%H:%M')
closed=datetime.strptime('17:00','%H:%M')

now_utc=datetime.now(timezone('UTC'))
print(now_utc.strftime(format))

now_london=now_utc.astimezone(timezone('Europe/London'))
now_portland=now_utc.astimezone(timezone('America/Los_Angeles'))
now_newyork=now_utc.astimezone(timezone('America/New_York'))

print(now_london.strftime(format))
print(now_portland.strftime(format))
print(now_newyork.strftime(format))


if now_london<opened and now_london>closed:
    print('Opened')
else:
    print('Closed')
    
