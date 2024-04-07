def isPalindrome(s): 
        start = 0
        end = len(s) - 1
        while(start<end):
            # print(start,end)
            # print(s[start], s[end])
            while not s[start].isalnum() and start<len(s)-1:
                # print("h1")
                start +=1
            while not s[end].isalnum() and end>0:
                # print("h2")
                end -=1 
            if start==end:
                return True
            elif start>end:
                return True
            elif start<end and s[start].lower()==s[end].lower():
                # print("here",s[start], s[end])
                start +=1
                end -=1
            else:
                return False
        return True
        
print(isPalindrome(".,"))