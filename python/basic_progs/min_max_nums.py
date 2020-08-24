def compute_min(array):
#function to compute minimum in a given array
    #first element of array is assumed as minimum and stored in variable min
    min = array[0]
    for x in array:
        #checks whether each element in array is less than 'min'
        if(x < min): 
            #if yes, store the value of that element in min
            min = x
    print(min)

def compute_max(array):
#function to compute maximum in a given array
    #first element of array is assumed as maximum and stored in variable max
    max = array[0]
    for y in array:
        #checks whether each element in array is greater than 'max'
        if(y > max):
            #if yes, store the value of that element in max
            max = y
    print(max)

if __name__ == "__main__":
    compute_min([3,5,1,7,9]) == 1
    compute_max([3,5,1,7,9]) == 9