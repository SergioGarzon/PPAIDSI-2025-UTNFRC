import datetime
import random

def generate_random_datetime_string(start_year, end_year):
    """
    Generates a random datetime string within a specified year range
    in 'yyyy-MM-dd hh:mm:ss' format.
    """
    start_date = datetime.datetime(start_year, 1, 1, 0, 0, 0)
    end_date = datetime.datetime(end_year, 12, 31, 23, 59, 59)

    # Convert dates to timestamps
    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())

    # Generate a random timestamp within the range
    random_timestamp = random.randint(start_timestamp, end_timestamp)

    # Convert the random timestamp back to a datetime object
    random_datetime_obj = datetime.datetime.fromtimestamp(random_timestamp)

    # Format the datetime object into the desired string format
    formatted_datetime_string = random_datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_datetime_string

# Example usage: Generate a random date and time between 2000 and 2025
random_date_time = generate_random_datetime_string(2000, 2025)
print(random_date_time)