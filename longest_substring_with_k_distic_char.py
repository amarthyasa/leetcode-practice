def longest_substring_with_k_distic_char(str1, k):
    window_start = 0
    window_end = 0
    char_freq = {}
    max_len = 0

    for window_end in range(0, len(str1)):
        r_char = str1[window_end]
        if r_char not in char_freq:
            char_freq[r_char] = 0
        char_freq[r_char] += 1
        window_end+=1

        while len(char_freq)>k:
            l_char = str1[window_start]
            char_freq[l_char]-= 1
            window_start+=1
            if char_freq[l_char]==0:
                del(char_freq[l_char])
        
        max_len = max(max_len, window_end - window_start)

    return(max_len)