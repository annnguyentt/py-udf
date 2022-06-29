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