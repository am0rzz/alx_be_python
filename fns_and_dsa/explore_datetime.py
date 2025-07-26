from datetime import datetime,timedelta,date


def display_current_datetime():
    cuurent_date = datetime.now().replace(microsecond=0)
    print(f"Current date and time: {cuurent_date}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = date.today() + timedelta(days=number_of_days)
    print(f"Future date: {future_date}")


display_current_datetime()
calculate_future_date()