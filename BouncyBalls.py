# ow3n
# 
# December 15, 2022
# 

def bouncing_ball(h, bounce, window):
    if (h > 0) and (0 < bounce < 1) and (window < h):
        count = 0
        while h > window:
            h *= bounce
            count += 1
        return (count*2) - 1
    else:
        return -1
