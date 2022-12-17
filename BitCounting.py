# ow3n
# 
# December 17, 2022
# 

# Write a function that takes an integer as input, 
# and returns the number of bits that are equal to one 
# in the binary representation of that number. 
# You can guarantee that input is non-negative.

def count_bits(n):
    binary = bin(n)
    count = 0
    for number in binary:
        if number == '1':
            count += 1
        else:
            pass
    return count

def main():
    count_bits(1)

if __name__ == "__main__":
    main()
