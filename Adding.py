


import spacy
import os
from date import get_date
from timeconv import get_time
import pandas as pd
from spacy.matcher import PhraseMatcher
from send import mail

def adder(user_name,user_input,nlp):
    doc = nlp(user_input)
    date_time_entities = {
        ent.label_: ent.text
        for ent in doc.ents
        if ent.label_ in ["DATE", "TIME"]
    }

    date_entity = get_date(date_time_entities.get("DATE", None))
    time_entity = get_time(date_time_entities.get("TIME", None))

    csv_file_path = "users.csv"
    df = pd.read_csv(csv_file_path)
    names = df['username'].tolist()

    def is_user_name(word):
        return word.lower() in [name.lower() for name in names]
    
    
  
    event_names = ["meeting", "presentation", "interview", "lunch", "deadline", "team call", "review"]
    


    
    doc = nlp(user_input)


    matcher = PhraseMatcher(nlp.vocab)
    event_patterns = [nlp(event) for event in event_names]
    matcher.add("EventMatcher", None, *event_patterns)


    user_names_found = [token.text for token in doc if is_user_name(token.text)]
    user_names_found.append(user_name)
    
    matches = matcher(doc)
    if matches:
        event_names_found = [doc[start:end].text for match_id, start, end in matches]
    else:
        event_names_found = ["Reminder"]
    
    mail(date_entity,time_entity,user_names_found,event_names_found)
    return date_entity,time_entity,user_names_found,event_names_found



