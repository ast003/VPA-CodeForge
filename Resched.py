import csv
import spacy
import os
from date import get_date
from timeconv import get_time
from number_parser import parse_ordinal


def rescheduler(user_name,user_input,nlp):
    doc = nlp(user_input)
    date_time_ordinal_entities = {
        ent.label_: ent.text
        for ent in doc.ents
        if ent.label_ in ["DATE", "TIME","ORDINAL"]
    }
    date_entity = get_date(date_time_ordinal_entities.get("DATE", None))
    time_entity = get_time(date_time_ordinal_entities.get("TIME", None))
    ordinal_entity=parse_ordinal(date_time_ordinal_entities.get("ORDINAL", None))
    return date_entity,time_entity,ordinal_entity
