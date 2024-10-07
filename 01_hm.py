from datetime import datetime

def get_days_from_today(date):
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")
    today = datetime.today().date()

    difference = (target_date.date() - today).days

    return difference

print(get_days_from_today('2024-10-15'))