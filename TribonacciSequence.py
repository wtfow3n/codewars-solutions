# ow3n
# 
# December 17, 2022
# 

# Create algorithm like Fibonacci, but summing the last 3 (instead of 2) 
# numbers of the sequence to generate the next integer.

def tribonacci(signature, n):
    
    if n == 0:
        return []
    if n < 3:
        return [signature[i] for i in range(0,n)]
    
    list = signature[:]
    
    for i in range(3,n):
        list.append(list[i-1] + list[i-2] + list[i-3])
        
    return list
    
def main():
    tribonacci([1, 1, 1], 10)
    
if __name__ == '__main__':
    main() 
