"""
top_one 
yoou can show the topest number in the array
and say how many time repide 

"""
def top (arr):
    values = {}
    result = []
    f_val = 0
    
    for i in arr:
        if i in values :
            values[i] += 1 
        else:
            values[i] = 1
            
    f_val = max (values.values())
    
    for i in values.keys():
       if values[i] == f_val :
           result.append(i)
       else:
           continue
    
    return result ,f_val


print (top([1, 2 , 3 , 5 , 8 , 8 , 8 , 9 , 9 , 7 , 9 , 9]))           
       
        