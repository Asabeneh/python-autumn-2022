def display_time():
    from datetime import datetime
    now = datetime.now()
    print(now)                      # 2021-07-08 07:34:46.549883
    day = now.day                   # 8
    month = now.month               # 7
    year = now.year                 # 2021
    hour = now.hour                 # 7
    minute = now.minute             # 38
    second = now.second
    return f'{day}/{month}/{year}, {hour}:{minute}:{second}'
 