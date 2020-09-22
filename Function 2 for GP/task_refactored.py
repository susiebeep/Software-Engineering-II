# the my_datetime function takes an integer value (num_sec) which represents
# the number of seconds since Jan 1st 1970 (the epoch). It then
# converts num_sec to a date and returns as a string in the format
# MM-DD-YY

# global vars
year = 1970
month = 1
day = 1


# validate input
def my_datetime_validate(num_sec):
    if str(num_sec).isdigit():
        if num_sec < 0:
            return -1
        if num_sec == 0:
            return 0
        else:
            return int(num_sec)
    else:
        return -1


# get number of days
def my_datetime_days(num_sec):
    sec_day = 86400
    num_days = num_sec / sec_day
    return num_days


# get number of years
def my_datetime_years(num_days):
    year_count = 0
    days_in_next_year = 365
    while (num_days - days_in_next_year) >= 0:
        num_days -= days_in_next_year
        year_count += 1
        if int(year + year_count) % 4 == 0:
            if int(year + year_count) % 100 == 0:
                if int(year + year_count) % 400 == 0:
                    days_in_next_year = 366
                else:
                    days_in_next_year = 365
            else:
                days_in_next_year = 366
        else:
            days_in_next_year = 365
    return year_count, num_days


# get number of months
def my_datetime_months(year_count, num_days):
    leap_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_count = 0
    if int(year + year_count) % 4 == 0:
        if int(year + year_count) % 100 == 0:
            if int(year + year_count) % 400 == 0:
                days_list = leap_days
        else:
            days_list = leap_days

    for day1 in days_list:
        if num_days - day1 >= 0:
            num_days -= day1
            month_count += 1
        else:
            break
    result = str(int(month + int(month_count))).zfill(2) + "-" + str(
        int(day + num_days)).zfill(2) + "-" + str(
            int(year + year_count))
    return result


def my_datetime(num_sec):
    valid_secs = my_datetime_validate(num_sec)
    if valid_secs < 0:
        return None
    num_days = my_datetime_days(valid_secs)
    year_count, days = my_datetime_years(num_days)
    return my_datetime_months(year_count, days)
