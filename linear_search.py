"""
linear(sequential)_search
    [1,2,3,5,8,11,14,18,23,32,48] 11 => 4


"""

def linear_search(array , element):
    for i in range (len(array)):
        if array [i] == element :
            return i 
        
        
    return -1

print (linear_search([1,2,3,5,8,11,14,18,23,32,48] , 11 ))