"""
    zigZagitrator
    [ 1 , 2 , 5 , 7 , 9] [ 3 , 4 , 6 , 8 , 9] = > 1,2,3,4,5,6,7,8,9
    


    
"""
class ZigZag :
    def __init__(self , l1 , l2 ):
        self.queue = (l1 , l2 )
        
    def next (self):
        v = self.queue.pop(0)
        r = v.pop(0)
        if v :
            self.queue.append(v)
        return r
    
    def has_next(self):
        if self.queue:
            return True
        return False
z = ZigZag ([ 1, 2 , 5 , 7 , 9][3 , 4 , 6 , 8])  
while z.has_next():
    print (z.next() , end = " ")
  