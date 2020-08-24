def parse_weblog_file(filename):
    #Creates a function of containing three elements (ip_address,URLs,bytes_received)
    log_entries = []
    #creates an empty list
    f = open(filename,'r')  
    lines = f.readlines()
    for line in lines:
        #to split the line into tokens
        token = line.split()
        ip_add = token[0]
        bytes_rec = token[9]
        url = token[6]
        #creates a tuple of three elements
        log_entry = (ip_add,url,bytes_rec)
        #tuple appended in list
        log_entries.append(log_entry)     
    return log_entries

 #1] FUNCTION TO COUNT UNIQUE IPs
def compute_uniq_ips(log_entries):
    #creates a set of unique IPs
    uniq_ip = set()
    for entry in log_entries:
        #takes entry from tuple and stores it in variable ip_add
        ip_add = entry[0]
        #adds each ip_add into set uniq_ip
        uniq_ip.add(ip_add)
        #returns the list of set
    return list(uniq_ip)    
   
#2] FUNCTION TO COUNT BYTES RECEIVED BY EACH IP_ADDRESS
def compute_greedy_clients(log_entries,top):
    #1)creates empty dictionary for bytes
    byte_dict = {}
    #for each entry in log_entries
    for entry in log_entries:
        #takes bytes received by each ip in bytes_rec
        bytes_rec = entry[2]
        #takes ip_address in variable ip_add
        ip_add = entry[0]
        try:
            #type conversion of string into integer
            bytes_rec = int (bytes_rec)
        except:
            #assigning 0 to '-'
            bytes_rec = 0
        if ip_add in byte_dict:
            #To add bytes of the same IP
            byte_dict[ip_add] += bytes_rec
        else:
            #Returns the bytes as it is
            byte_dict[ip_add] = bytes_rec
            #sorting in descending order
        sort_dict = sorted(byte_dict.items(), key=lambda x: x[1], reverse= True)
    return sort_dict[:top]
               
#3] FUNCTION TO COUNT FAMOUS URLs
def compute_famous_urls(log_entries,howmany):
    #creates an empty dictionary to store URLs 
    url_dict = {}
    for entry in log_entries:
        #stores entry from tuple into variable url
        url = entry[1]  
        if url in url_dict:
            #to increase the count of URL when found
            count = url_dict[url] + 1
            #to assign the new count 
            url_dict[url] = count
        else:
            url_dict[url] = 1
    #sorting in descending order
    sort_dict = sorted(url_dict.items(), key=lambda x: x[1], reverse= True)
    return sort_dict[:howmany]

#TESTCASES   
if __name__ == "__main__":
    filename = 'weblog.txt'
    log_entries = parse_weblog_file(filename)
    print(compute_uniq_ips(log_entries))
    print(compute_famous_urls(log_entries,5))
    print(compute_greedy_clients(log_entries,2))
