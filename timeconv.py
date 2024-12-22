from dateutil import parser

def get_time(input_time):
    try:
        parsed_time = parser.parse(input_time)
        return parsed_time.strftime("%H:%M:%S")
    except ValueError:
        return "Invalid input time format"

