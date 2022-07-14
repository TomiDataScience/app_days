year_days=365
year_week=52
year_month=12
dead_year=90
current_year=input("What is the current year?")
remains_year=dead_year-int(current_year)
remains_month=remains_year*year_month
remains_week=remains_month*year_week
remains_days=remains_month*year_days
print("You have", remains_days, "days", remains_week, "week", remains_month, "month left in your life.")