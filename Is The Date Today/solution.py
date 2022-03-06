from datetime import datetime

def is_today(date):
    return date.strftime('%Y-%m-%d') == datetime.today().strftime('%Y-%m-%d')
