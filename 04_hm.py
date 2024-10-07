from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
   
    upcoming_birthdays = []
    today = datetime.today().date()

    for user in users:
        
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        birthday_this_year = birthday.replace(year=today.year)

        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        
        days_until_birthday = (birthday_this_year - today).days

        
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "Віра", "birthday": "2024.10.08"},
    {"name": "Віталій", "birthday": "2024.10.10"},
    {"name": "Валерій", "birthday": "2024.10.12"},
    {"name": "Елеонора", "birthday": "2024.10.13"},
    {"name": "Катерина", "birthday": "2024.10.07"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print(upcoming_birthdays)