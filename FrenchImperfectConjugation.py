# ow3n
# 
# December 15, 2022
# 

def to_imparfait(verb_phrase):
    verb_phrase2 = verb_phrase[:-2]
    if verb_phrase[:2] == 'Je' or verb_phrase[:2] == 'Tu':
        verb_phrase2 = verb_phrase2 + "ais"
    elif verb_phrase[:3] == 'Ils' or verb_phrase[:5] == 'Elles':
        verb_phrase2 = verb_phrase2 + "aient"
    elif verb_phrase[:4] == 'Elle' or verb_phrase[:2] == 'Il' or verb_phrase[:2] == 'On':
        verb_phrase2 = verb_phrase2 + "ait"
    elif verb_phrase[:4] == 'Nous':
        verb_phrase2 = verb_phrase2 + "ions"
    elif verb_phrase[:4] == 'Vous':
        verb_phrase2 = verb_phrase2 + "iez"

    return(verb_phrase2)
