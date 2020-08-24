def compute_gcd(a,b):
    i = 1
    while(i <= a and i <= b):
        #checking if i is perfectly divisible to both a and b
        if(a % i == 0 and b % i == 0):
            c = i
        #increasing count will give the highest number i.e. GCD
        i = i + 1
    print("The GCD is ",c)

if __name__ == "__main__":
    compute_gcd(48,60)
    compute_gcd(12,14)
    compute_gcd(24,54)
    