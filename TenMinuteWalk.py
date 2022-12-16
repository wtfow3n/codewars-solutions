# ow3n
# 
# December 15, 2022
# 

def is_valid_walk(walk):
    if len(walk) != 10: # check if a valid walk
        return False
    else:
        x = ''.join(walk) # turn list into string
        n=0
        e=0
        s=0
        w=0
        for dir in x: # parse string char by char
            if dir == 'n':
                n+=1
            elif dir == 'e':
                e+=1
            elif dir == 's':
                s+=1
            elif dir == 'w':
                w+=1

        if (n-s == 0 and e-w == 0): # check to see if directions cancel eachother out...
            return True
        else:
            return False
