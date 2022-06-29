
import time
from datetime import datetime, timezone, timedelta

# convert convert_unix_to_localtime

def convert_unix_to_localtime(x, date_format='%Y-%m-%d %H:%M:%S'):
    hour = (time.timezone if (time.localtime().tm_isdst == 0) else time.altzone) / 60 / 60 * -1
    tz = timezone(+timedelta(hours=hour))
    return datetime.fromtimestamp(x, tz).strftime(date_format)

# generate a dict for number formating
def generate_format_dict(df):
    format_dict = {}
    cols = dict(df.dtypes)
    for k,v in cols.items():
        if re.search('%|pct', k):
            format_dict[k] = '{:,.2%}'
        elif v in ['float64', 'int64']:
            format_dict[k] = '{:,.2f}'
    return format_dict