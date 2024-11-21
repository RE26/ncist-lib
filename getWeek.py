
from datetime import datetime, date
def getWeek():
    dayOfWeek = datetime.today().weekday()
    print(dayOfWeek + 1)
    return dayOfWeek + 1
