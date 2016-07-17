import calendar
import datetime

__author__ = 'Elfix'


def convert_month_name_to_date_range(month_name, year=None):
    """
    returns two python datetime object for beginning and end of a month
    example :
        convert_month_name_to_date_range("september",2000) will returns
    :param month_name: the month to use in calculating the datetime object
    :param year: the year to use in calculating the datetime object , it will use current year if year = None
    :return: a tuple of length two for beginning and end of the month
    """
    if year is None:  # checking if year parameter is None
        year = datetime.datetime.now().year  # set year to current year
    month_name = month_name.capitalize()
    month_names = list(calendar.month_name)
    if month_name not in month_names:  # checking for invalid month name like Jooly instead of july
        raise ValueError("Invalid month name provided")
    month_number = month_names.index(month_name)  # convert month name to month number
    month_length = calendar.monthrange(year, month_number)[1]  # get number of day in the specific month
    return datetime.date(year, month_number, 1), datetime.date(year, month_number, month_length)
    # return tuple of start date and end date
