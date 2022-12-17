# ow3n
# 
# December 17, 2022
# 

# Your code must return true or false (not 'true' and 'false') 
# depending upon whether the given number is a Narcissistic number 
# in base 10. This may be True and False in your language, e.g. PHP.

def narcissistic(value):
    
    exponent = len(str(value))
    list = []
    number = 0
    
    for digit in iter(str(value)):
        list.append(digit)
    
    for i in range(0, len(str(value))):
        number += int(list[i]) ** int(exponent)
    
    if number == value:
        return True
    else:
        return False
        
def main():
    narcissistic(7)
    
if __name__ == '__main__':
    main() 
