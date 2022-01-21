from datetime import datetime, timezone
from dateutil import  parser,tz
from pytz import timezone

format="%H:%M"

opened=parser.parse('8:00')
opened=opened.replace(tzinfo=tz.gettz("Europe/London"))
closed=parser.parse('17:00')
closed=closed.replace(tzinfo=tz.gettz("Europe/London"))

now_utc=datetime.now(timezone('UTC'))

now_london=now_utc.astimezone(timezone('Europe/London'))
now_portland=now_utc.astimezone(timezone('America/Los_Angeles'))
now_newyork=now_utc.astimezone(timezone('America/New_York'))


if now_london>opened and now_london<closed:
    print('London is Opened {}'.format(now_london))
else:
    print('London is Closed {}'.format(now_london))

opened=parser.parse('8:00')
opened=opened.replace(tzinfo=tz.gettz("America/Los_Angeles"))
closed=parser.parse('17:00')
closed=closed.replace(tzinfo=tz.gettz("America/Los_Angeles"))

if now_portland>opened and now_portland<closed:
    print('Portland is Opened {}'.format(now_portland))
else:
    print('Portland is Closed {}'.format(now_portland))

opened=parser.parse('8:00')
opened=opened.replace(tzinfo=tz.gettz("America/New_York"))
closed=parser.parse('17:00')
closed=closed.replace(tzinfo=tz.gettz("America/New_York"))

if now_newyork>opened and now_newyork<closed:
    print('New York is Opened {}'.format(now_newyork))
else:
    print('New York is Closed {}'.format(now_newyork))

#print(now_london.strftime(format))
#print(now_portland.strftime(format))
#print(now_newyork.strftime(format))
