

import datetime, bday_messages

today = datetime.date.today()

next_bday = datetime.date(today.year, 12, 31)

time_diffrence = next_bday - today

days_away = time_diffrence.days

if days_away == 0:
    print(bday_messages.random_message)

else:
    print(f'Your birthday is {days_away} days away! 🎉')