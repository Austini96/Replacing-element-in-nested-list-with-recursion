# Example:
#   >>> L=[1, [3, 1, [4, -1], 2], [[[5]]], [1, 3]]
#   >>> replace_elem(L, 1, 'a')
#   >>> L
#   ['a', [3, 'a', [4, -1], 2], [[[5]]], ['a', 3]]

def replace_elem(L, old, new):
    for i in range(len(L)): # for loop to check every element in the list
        if not isinstance(L[i], list): # if ith element is not a list and the element is 'old', replace with 'new'
            if L[i] == old:
                L[i] = new
        elif L == []: # continue on if L is an empty list
            continue
        elif isinstance(L[i], list): # if ith element is a list, run the function again with the ith element of L
            replace_elem(L[i], old, new)
