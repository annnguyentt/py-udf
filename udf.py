
import time
from datetime import datetime, timezone, timedelta

# convert convert_unix_to_localtime

def convert_unix_to_localtime(x, date_format='%Y-%m-%d %H:%M:%S'):
    hour = (time.timezone if (time.localtime().tm_isdst == 0) else time.altzone) / 60 / 60 * -1
    tz = timezone(+timedelta(hours=hour))
    return datetime.fromtimestamp(x, tz).strftime(date_format)

if __name__ == '__main__':
    convert_unix_to_localtime(1656115226)