import calendar
import datetime


def get_range_dates_metadata_yearly(date):
    # TODO: check on date
    if date is not None:
        year = int(date[:4])
        # month = int(date[4:])
        return get_range_dates_metadata_yearly(year)
    return None


def get_range_dates_metadata_yearly(year):
    from_date = datetime.datetime(int(year), int(1), 1)
    last_day = calendar.monthrange(int(year), int(12))[1]
    to_date = datetime.datetime(int(year), int(12), last_day)
    from_date_result = calendar.timegm(from_date.timetuple()) * 1000
    to_date_result = calendar.timegm(to_date.timetuple()) * 1000
    return from_date_result, to_date_result
