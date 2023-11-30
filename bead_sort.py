"""
    bead sort 
        [ 4 , 7 , 5 , 8 , 9 , 6 , 14 , 12 , 31 , 25 ]


"""

def bead_sort (sequence):
    if any(not isinstance(x , int)or x < 0 in sequence):
        raise TypeError("sequence must be list of non-nagative integers")
    
    for _ in range (len (sequence)):
        for i , (rod_upper , rod_lower ) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i+1] += rod_upper - rod_lower
                
    return sequence
print (bead_sort ([4 , 7 , 2 , 9 , 3 , 6 5]))