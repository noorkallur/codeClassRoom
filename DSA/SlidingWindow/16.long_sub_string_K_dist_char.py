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

# revisited  the question
def long_sub_str_with_k_dist_char(str, target):
    hm = {}
    max_sub_len = 0
    for i in range(len(str)):
        if len(hm) == target and not str[i] in hm: # check if hm reaches target len and new char is being added
            max_sub_len = max(max_sub_len, sum(hm.values())) # update the max len 
            hm.pop(list(hm.keys())[0]) # pop the index 0 of the hashmap (hashmap is orderd)

        hm[str[i]] = hm.get(str[i], 0) + 1 # add the new char in the hashmap

    return max_sub_len
       
str = "aaahhibc"# 5
k = 2
str = "ecebaa" # 3
k = 2
str = "aabacccac" # 3
k = 1
print(long_sub_str_with_k_dist_char(str, k))
            
            
            
            
