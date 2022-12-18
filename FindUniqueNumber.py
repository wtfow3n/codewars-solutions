# ow3n
# 
# December 17, 2022
# 

# There is an of numbers, find out which number is  
# not like the others

def find_uniq(arr):
    
    arr.sort()
    
    if arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]:
        n = arr[0]
    else:
        n = arr[len(arr)-1]
        
    return n
            
def main():
    find_uniq([ 0, 0, 0.55, 0, 0, 0 ])
    
if __name__ == "__main__":
    main()
