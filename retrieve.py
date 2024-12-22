import csv
def retrieve_data(user_name):
    commands = []

    
    file_path = f"{user_name}.csv"

    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
           
            next(csvreader, None)
            
            for row in csvreader:
                commands.append(row)
    except FileNotFoundError:
        
        pass

    return commands