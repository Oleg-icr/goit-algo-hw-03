from datetime import datetime


def get_days_from_today(date):
    date = datetime.strptime(date, "%Y-%m-%d").date()

    return date


print ( get_days_from_today("2025-02-03") )