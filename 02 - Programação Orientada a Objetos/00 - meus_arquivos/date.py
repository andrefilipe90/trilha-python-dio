from datetime import date, datetime
import time

print(date.today())

while True:
    array = ["--","\\","|","/"]
    for item in array:
        time.sleep(0.05)
        print(item.center(5,' '),end='')
        print(datetime.today())