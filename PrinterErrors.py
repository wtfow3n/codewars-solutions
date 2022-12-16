# ow3n
# 
# December 15, 2022
# 

def printer_error(s):
    
    numerator = 0
    denominator = len(s)
    
    for letter in s:
        if ord(letter) > 109:
            numerator += 1
        else:
            pass
    
    return(str(numerator) + "/" + str(denominator))
