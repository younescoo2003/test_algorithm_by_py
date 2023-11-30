"""
    remove min
    [ 4 , 5 , 8 , 2 , -2 , 0] => -2

"""

def remove_min(stack):
    storage_stack = []
    if len(stack) == 0 :
        return stack
    
    min = stack.pop()
    stack.append(min)
    for i in range (len(stack)):
        val = stack.pop()
        if val <= min :
            min = val 
        storage_stack.append(val)
        
    for i in range (len(storage_stack)):
        val = storage_stack.pop()
        if val != min :
            stack.append(val)
            
    return stack , min 
print (remove_min([ 4 , 5 , 8 , 2 , -2 , 0]))