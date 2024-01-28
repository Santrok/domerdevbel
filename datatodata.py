import time
from datetime import datetime, date, timedelta

today = datetime.now()
sec = time.time()
yesterday = date(day=17, month=1, year=2024)
yesterday2 = date(day=1, month=2, year=2024)
print(date.fromtimestamp(sec))
# print(yesterday)
# print(today.date() - yesterday)
print(yesterday2-timedelta(1))
