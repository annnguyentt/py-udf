# convert convert_unix_to_localtime

import time
from datetime import datetime, timezone, timedelta

def convert_unix_to_localtime(x, date_format='%Y-%m-%d %H:%M:%S'):
    hour = (time.timezone if (time.localtime().tm_isdst == 0) else time.altzone) / 60 / 60 * -1
    tz = timezone(+timedelta(hours=hour))
    return datetime.fromtimestamp(x, tz).strftime(date_format)