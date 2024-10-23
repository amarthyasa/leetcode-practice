def longestPalindrome(words) -> int:
        h = {}
        for i in words:
            if i[::-1] not in h:
                h[i] = []
            else:
                if len(h[i[::-1]]) <1:
                    h[i[::-1]].append(i)
                else:
                    h[i] = []
        
        # for key in h.keys():
        #     if len(h[key])!=0
        #         if len(h[key])%2 !=0:
        #             output = output + 

        print(h)



        
        

longestPalindrome(["ab","ba","ba","ab","ab","ba","ba","ab"])