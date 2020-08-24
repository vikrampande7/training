def convert_base(number,base):
    #Function to convert decimal into binary, octal, hexadecimal
    if base == 'binary':
        integer = int(number)
        print (number , "in binary: ",bin(integer))
    elif base == 'octal':
        integer = int(number)
        print (number , "in binary: ",oct(integer))
    elif base == 'hexadecimal':
        integer = int(number)
        print (number , "in binary: ",hex(integer))
#Testcases
if __name__ == "__main__":
    number = 31
    convert_base(number,'binary')
    convert_base(number,'octal')
    convert_base(number,'hexadecimal')
