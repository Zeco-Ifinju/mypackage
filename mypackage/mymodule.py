def top_n (item, n):
    '''this going to return the top n item of an array in a decending order.
    
    Args:
    
    item [array]: list or array-like object 
    n(int) the number of items to return 
    
    return
    array : top n items in decending order 
    
    eg
    >>> top_n([8, 3, 2, 7, 4], 3)
    [8, 7, 4] 
    '''

    for i in range(n): # keep sorting until we have the nth termm 
        for j in range(len(item)-1 -i):

            if item[j] > item[j + 1]: # if this item is greater than that item
                itme[j], item[j + 1] = item[j + 1], item[j] # swap the two

    # getting the last two item
    top_n = item[-n:]

    # return in decending order
    return top_n[: : -1]
    