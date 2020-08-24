def print_lines(filename,odd=None,nums=True):
    """
    To print lines in a given sample file
    Odd  = to rpint even or odd lines
    Nums = TO print lines with or without index
    """
    #print (filename,odd,nums)
    f = open(filename,'r')
    lines = f.readlines()
    count = 0
    for line in lines:
        count = count + 1
        #even
        if odd is False:
            if (count % 2 == 0):
                #To print with index
                if nums is True:
                    print(count,line)
                #To print without index
                else:
                    print(line)
        #Odd
        elif odd is True:
            if (count % 2 == 1):
                #To print with index
                if nums is True:
                    print(count,line)
                else:
                    print(line)
        #All        
        else:
            if nums is True:
                print(count,line)
            if nums is False:
                print(line)

def find_word(filename,word,ignore_case,match_word):
#Function to search a word from
    f = open(filename,'r')
    fh = f.readlines()
    for x in fh:
        if ignore_case == True:
            if match_word == True:
                low = x.lower()
                word = word.lower() 
                if word in low:
                    print(x)
            elif match_word == False:
                splitted = x.split()  
                if word in splitted:
                    print(x)       
        elif ignore_case == False:
            print("Not Found")
            
    
                    
#None used as null variable or object
if __name__ == "__main__":

    """
    print_lines('sample.txt') #Prints all the lines with index starting at 1
    print_lines('sample.txt',True,True) #odd lines with index 
    print_lines('sample.txt',True,False) #odd lines without index
    print_lines('sample.txt',False,True) #Even lines with index
    print_lines('sample.txt',False,False) #Even lines without index
    """
    print_lines('sample.txt',nums=False)
    find_word('sample.txt','coNs',True,True)