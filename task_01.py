from datetime import datetime, timedelta


def get_days_from_today(specified_date):
    # current day
    date_today = datetime.now().date()
    # check ValueError
    try:
        # transform specified date to string
        specified_date = datetime.strptime(specified_date, "%Y-%m-%d").date()
        # calculate difference between two dates
        difference = date_today - specified_date
        return difference.days
    except ValueError:
        print("Wrong entered date or wrong format date. Correct format is YYYY-MM-DD")


print ( get_days_from_today("2025-05-03") )
print ( get_days_from_today("2025-01-21") )
print ( get_days_from_today("2025.04.19") )
print ( get_days_from_today("2025.13.32") )
print ( get_days_from_today("2025-13-32") )