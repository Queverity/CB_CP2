# CB 1st Word Count Time Handling



# define function find_datetime():
    # current_time = date.datetime.now()
    # return current_time

from datetime import datetime

def find_datetime(datetime):
    current_time = datetime.now()

    year = current_time.year
    month = current_time.month
    day = current_time.day

    date = f"{year}-{month}-{day}"

    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second
    second = round(second,2)

    time = f"{hour}:{minute}:{second}"
    
    date_time = f"{date} {time}"

    return date_time
