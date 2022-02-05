"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
   Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
   
   Örnek olarak:

   input: [[1, 2], [3, 4], [5, 6, 7]]

   output: [[[7, 6, 5], [4, 3], [2, 1]]
   
"""

def reverseList(L):
    
    # the constraint block of the recursion
    if len(L) == 0:
        return
    
    # L might be a list or an element. If the length of L is 1, then we need to check if it is a list. 
    # If it is a list, then we will recall the function. If not so, we will return L, which is equivalent to an element in the initial input L.
    
    # There is another case that the length of L is greater than 1, which means that L contains items more than 1. So, we will recall the function twice. 
    # In the first recall of the function, the input will be the slice from 1st index to the end of the L.
    # In the second recall of the function, the input will be the first item of L.
    # The reason why that is done is to decrease the length of L in each time. 
    
    if len(L) == 1:
        if type(L[0] == list)
            return [reverseList(L[0])]
        else:
            return L
    else:
        return reverseList(L[1:]) + reverseList(L[0])
      
      
