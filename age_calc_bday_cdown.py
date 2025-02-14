import datetime

user_input = input("Please enter your birth-date in the yyyy-mm-dd format: ")

user_bday = datetime.date.fromisoformat(user_input)

today_date = datetime.date.today()

user_next_bday = datetime.date(today_date.year, user_bday.month, user_bday.day)

if user_next_bday < today_date:
    user_next_bday = user_next_bday.replace(year = today_date.year + 1)

days_until_bday = (user_next_bday - today_date).days

print(f'There are {days_until_bday} days until your next birthday!')

user_last_bday = user_next_bday.replace(year = user_next_bday.year - 1)

age_years = user_last_bday.year - user_bday.year
remainder_days = (today_date - user_last_bday).days

print(f'You are {age_years} years and {remainder_days} days old!')