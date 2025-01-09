import datetime

def get_time():
    strfTime = datetime.datetime.now().strftime("%H:%M:%S")
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        return "Good Morning Madam!"
    elif 12 <= hour < 18:
        return "Good Afternoon Madam!"
    else:
        return "Good Evening Madam!"
    return f"Madam the current time is {strfTime}"