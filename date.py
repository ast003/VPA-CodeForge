import dateparser
from datetime import datetime
from dateutil.relativedelta import relativedelta, MO

def get_date(relative_expression):
    
    reference_date = datetime.now()

   
    weekday_mapping = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    
    if relative_expression.isdigit()==False and relative_expression.lower() in weekday_mapping:
  
        next_weekday = reference_date + relativedelta(weekday=weekday_mapping[relative_expression.lower()])
        return next_weekday.date()
    else:
       
        parsed_date = dateparser.parse(relative_expression, settings={'RELATIVE_BASE': reference_date})

        if parsed_date:
            return parsed_date.date()
        else:
         
            raise ValueError("Failed to parse the relative expression")


