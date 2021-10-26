def power(x, e, m):
    res = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    x = x % m
     
    if (x == 0) :
        return 0
 
    while (e > 0) :
         
        # If y is odd, multiply
        # x with result
        if ((e & 1) == 1) :
            res = (res * x) % m
 
        # y must be even now
        e = e >> 1      # y = y/2
        x = (x * x) % m
         
    return res