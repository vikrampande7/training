def sort_ascending(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if(array[j] > array[j+1]):
                temp = array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    print("The sorted ascending ordered array is: ",array)

def sort_descending(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if(array[j] < array[j+1]):
                temp = array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    print("The sorted descending ordered array is: ",array)

def reverse(array):
    for i in range((int(len(array)/2))):
        array[i],array[-(i+1)]=array[-(i+1)],array[i]
    print(array) 

if __name__=="__main__":
    sort_ascending([15,4,34,12,45])
    print(sort_descending([15,4,34,12,45]))
    reverse([1,2,3,4,5,6,7,8])