"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
   Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 

   Örnek olarak:

   input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

   output: [1,'a','cat',2,3,'dog',4,5]

"""

def flatter(lst):
    
    # an empty list to add all items in lst
    output = []
    
    # create a second function so that output is not defined as an empty list in each turn
    def helper(lst):
      
      # create a "for loop" to travel in lst and nested-list items
        for item in lst:
          
            # if item is a list, then use a recall function to check if there is a list/lists in item
            if type(item) == list:
                helper(item)
                
            # if item is not a list, then add it into output    
            else:
                output.append(item)
    
    # call nested function
    helper(lst) 
    
    # return output 
    return output

