# ow3n
# 
# December 15, 2022
# 

def dig_pow(n, p):
    if n > 0 and p > 0:
        number = 0
        power = p - 1
        for digit in str(n):
            power += 1
            digit = int(digit)
            number += (digit**(power))
        if (number / n).is_integer():
            return (number / n)
        else:
            return -1
    else:
        return -1
