import datetime

# User must input in this format. Currently, no check is being implemented if user enters the incorrect format
user_input = input("Please enter your birth-date in the yyyy-mm-dd format: ")

user_bday = datetime.date.fromisoformat(user_input)

today_date = datetime.date.today()

# Initially this will calculate the user's birtday in the current calender year
user_next_bday = datetime.date(today_date.year, user_bday.month, user_bday.day)

# Here, if the user's birthday has already passed, this updates with the user's birthday next year
if user_next_bday < today_date:
    user_next_bday = user_next_bday.replace(year = today_date.year + 1)

days_until_bday = (user_next_bday - today_date).days

print(f'There are {days_until_bday} days until your next birthday!')

# Using the calculated value of user's next birthday to calculate what user's last birthday was
user_last_bday = user_next_bday.replace(year = user_next_bday.year - 1)

# Then using that value to calculate age in years and days
age_years = user_last_bday.year - user_bday.year
remainder_days = (today_date - user_last_bday).days

print(f'You are {age_years} years and {remainder_days} days old!')