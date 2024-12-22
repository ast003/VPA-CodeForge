import csv
import ast

def modify_data_point(user_name, index, new_date, new_time):
    
    fieldnames = ['primary_key', 'date', 'time', 'event', 'Along_with']
    file_path = f"{user_name}.csv"
    primary=0
    
        
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        data = list(csvreader)

  
    if 0 <= index < len(data):
       
        primary= data[index][0] 
          
    else:
        print("Invalid index.")

 

    along=[]
    with open("schedule.csv", 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        
        for row in csvreader:
            if row['primary_key'] == primary:
                along=row["Along_with"]
    
    along = ast.literal_eval(along)
    for user in along:
   
        
        with open(f"{user}.csv", 'r+', newline='', encoding='utf-8') as userfile:
            user_reader = csv.DictReader(userfile)
            user_data = list(user_reader)

            for entry in user_data:
                if entry['primary_key'] == primary:
                   
                    entry['date'] = new_date
                    entry['time'] = new_time

            userfile.seek(0)
            userfile.truncate()
            user_writer = csv.DictWriter(userfile, fieldnames=user_reader.fieldnames)
            user_writer.writeheader()
            user_writer.writerows(user_data)        