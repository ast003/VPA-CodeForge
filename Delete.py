import spacy
import os
from number_parser import parse_ordinal




def delete(user_name,user_input,nlp):
    doc = nlp(user_input)
    ordinal_entities = {
        ent.label_: ent.text
        for ent in doc.ents
        if ent.label_ in ["ORDINAL"]
    }
    ordinal_entity=parse_ordinal(ordinal_entities.get("ORDINAL", None))
    return ordinal_entity
