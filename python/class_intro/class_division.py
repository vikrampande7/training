class division:

    def __init__(self,numerator,denominator):
        self.__num = numerator
        self.__denom = denominator

    def perform_division(self):
        if self.__denom == 0:
            return "Infinity"
        else:
            return (self.__num/self.__denom)

    def __repr__(self):
        return 'division numerator = %s, denominator = %s' % (self.__num,self.__denom)
        
if __name__ == "__main__":

    d = division(60,0)
    print (d.__repr__())
    print (d.perform_division())