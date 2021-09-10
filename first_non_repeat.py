def firstNotRepeatingCharacter(s):
    char_order = []
    ctr = {}
    for c in s:
        if c in ctr:
            ctr[c] +=1
        else:
            ctr[c] = 1
            char_order.append(c)
    for c in char_order:
        if ctr[c]==1:
            return c
    return '_'
    
    

