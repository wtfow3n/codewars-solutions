# ow3n
# 
# December 15, 2022
# 

def xo(s):
    x=0
    o=0
    string = s.lower()
    for letter in string:
        if letter == 'x':
            x+=1
        elif letter == 'o':
            o+=1
        else:
            pass
    if x==o:
        return True
    else:
        return False
