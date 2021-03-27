import re
import pandas as pd
from datetime import datetime
# from src.utils.logging_util import Logger

# LOGGER = Logger.get_instance()


def get_date_time(date_string):
    try:
        if not pd.isna(date_string):
            regex = r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]|(?:JAN|MAR|MAY|JUL|AUG|OCT|DEC|Jan|Mar|May|Jul|Aug|Oct|Dec|jan|mar|may|jul|aug|oct|dec)))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2]|(?:JAN|MAR|MAY|JUL|AUG|OCT|DEC|Jan|Mar|May|Jul|Aug|Oct|Dec|jan|mar|may|jul|aug|oct|dec))\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)(?:0?2|(?:Feb))\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9]|(?:JAN|MAR|MAY|JUL|AUG|OCT|DEC|Jan|Mar|May|Jul|Aug|Oct|Dec|jan|mar|may|jul|aug|oct|dec))|(?:1[0-2]|(?:OCT|NOV|DEC|Oct|Nov|Dec|oct|nov|dec)))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})"
            test_str = date_string
            matches = re.finditer(regex, test_str, re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
                if match.group() is not None:

                    return match.group()
                else:

                    date = date_string.split(" ")[0]
                    return date
            else:
                date = date_string.split(" ")[0]

                return date
        else:
            return date_string

    except Exception as e:
        pass
        # print(e)
        # import pdb
        # pdb.set_trace()
    return date_string


min_date = "01-FEB-1980"
min_date = datetime.strptime(min_date, '%d-%b-%Y').strftime('%d-%m-%y')
min_date_object = datetime.strptime(min_date, '%d-%m-%y')

def validate_trundate(row,min_date=min_date_object):
    try:
        date_val =  datetime.strptime(row, '%d-%b-%y').strftime('%d-%m-%y')
        date_val = datetime.strptime(date_val, '%d-%m-%y')
        maxDate = max(datetime.strptime("22-03-21", '%d-%m-%y'),datetime.today())
        if min_date <= date_val <= maxDate:
            return datetime.strftime(date_val, '%d-%b-%y')
        else:
            return None
    except Exception as e:
        pass
        # print(e)
    return row

