# https://youtu.be/MK-NZ4hN7rs?si=m28WmClU33LdyL8x&t=1987

def long_sub_str_with_k_dist_char(str, k):        
    hash_map ={}
    max_sub_len = 0
    win_start = 0
    for win_end in range(0, len(str)):
        
        #add to hash_map
        if str[win_end] in hash_map: 
            hash_map[str[win_end]] += 1
        else:
            hash_map[str[win_end]] = 1
                         
        #hash map exceeded the distinct letters 
        while len(hash_map) > k:
            hash_map[str[win_start]] -= 1 #remove the first one
            if hash_map[str[win_start]] == 0: # if the key reaches zero remove it
                hash_map.pop(str[win_start])
            win_start += 1 #increment first index
        
        max_sub_len =max(sum(hash_map.values()), max_sub_len)
    
    return max_sub_len  
        
str = "aaahhibc"
k = 2
str = "ecebaa"
k = 2
str = "aabacccac"
k = 1
print(long_sub_str_with_k_dist_char(str, k))
            
            
            
            
