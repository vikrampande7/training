#Function to convert base of a given integer
def convert_int_to_base(number , base):
    integer = int(number)
    #base = base.lower()
    #To convert number in binary equivalent
    if base == 'bin':
        #Creates an empty list to store remainders
        binary_list = []
        #loop till integer is greater than zero
        while integer > 0:
            #gets remainder of the number
           rem = integer % 2
           #appends the remainder into empty list created 
           binary_list.append(rem)
           #for quotient
           integer = int(integer/2)
        #output is reversed
        binary_list.reverse()
        #converts each element into str and returns
        join_list = "".join(str(each) for each in binary_list)
        return join_list
    
           
    #To convert number into Octal equivalent    
    if base == "oct":
        #Creates an empty list to store remainders
        octal_list = []
        #loop till integer is greater than zero
        while integer != 0:
            #gets remainder of the number
           rem = integer % 8
           #appends the remainder into empty list created 
           octal_list.append(rem)
           #for quotient
           integer = int(integer/8)
        #output is reversed
        octal_list.reverse()
        #converts each element in list into str and returns
        join_list = "".join(str(each) for each in octal_list)
        return join_list
    
    #To convert number into Hexadecimal equivalent
    elif base == "hex":
        #Creates an empty list to store remainders
        hexa_list = []
        hex_dict = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        #loop till integer is greater than zero
        while integer != 0:
            #gets remainder of the number
            rem = integer % 16
            if rem in hex_dict.keys():
                rem = hex_dict.get(rem)
           #appends the remainder into empty list created 
            hexa_list.append(rem)
           #for quotient
            integer = int(integer/16)
        #output is reversed
        hexa_list.reverse()
        #returns each element in list by convertimg in into str
        join_list = "".join(str(each) for each in hexa_list)
        return join_list

#A common function for any base
def convert_into_base_new(integer,base):
    #Creates an empty list to store remainders
    digits = []
    #string of all hex values
    hex_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    while integer > 0:
        #gets remainder of a number
        remainder = integer % base
        integer = integer // base 
        #appends the remainder and quotient values into list 'digits'
        digits.append(hex_digits[remainder])
    #list is revered
    digits.reverse()
    #to join two lists
    join_list = "".join(digits)
    return join_list

"""
The join() method is a string method 
and returns a string in which the elements of sequence have been joined by str separator.
Return Value: The join() method returns a string concatenated with the elements of iterable.
"""
if __name__ == "__main__":
    """
    integer = 1200
    print(convert_int_to_base(integer,"Bin"))
    print('\n')
    print(bin(integer))
    print('\n')
    print(convert_int_to_base(integer,"Oct"))
    print('\n')
    print(oct(integer))
    print('\n')
    print(convert_int_to_base(integer,"Hex"))
    print('\n')
    print(hex(integer))
    print('\n')
    """
    print(convert_into_base_new(30,16))
    print(convert_into_base_new(30,8))
    print(convert_into_base_new(30,2))
    
    



 