
import csv

def save_to_csv(date, time, user_found, events_found):

    fieldnames = ['primary_key', 'date', 'time', 'event', 'Along_with']

    existing_data = []
    
    with open("schedule.csv", 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        existing_data = list(csvreader)

    max_primary_key = max(int(record['primary_key']) for record in existing_data) if existing_data else 0
    
    
    with open('schedule.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'primary_key': max_primary_key+1, 'date': date, 'time': time, 'event': events_found, 'Along_with': user_found})
    
    for user in user_found:
        with open(user+".csv",'a',newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()
            
            writer.writerow({'primary_key': max_primary_key+1, 'date': date, 'time': time, 'event': events_found, 'Along_with': user_found})
       
