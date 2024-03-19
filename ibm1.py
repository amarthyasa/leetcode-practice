def getMinimumMoves(price, k):
    # Write your code here
    m= 100
    price.sort()
   
    median = int((len(price) + 1) / 2) -1
    print("median", median)
    for i in range(0, len(price)):
        if (abs(price[i] - k)) < m:
            m =  abs(price[i] - k)
            position = i
            print("diff", "i", m,i)
    
    if position < median:
        for i in range(position, median):
            if(price[i] > k):
                m = m + abs(price[i] - k)
                print("i, m", i, m)
                   
    if position > median:
        for i in range(position, median):
            if(price[i] < k):
                m = m + abs(price[i] - k)
                print("i, m", i, m)
    return m 

    
    
    
print(getMinimumMoves([3,3,6,3,9], 2))
print(getMinimumMoves([1,2,3], 5))