'''
Created on Nov 30, 2018

@author: penumr
'''
# Python program for implementation of Selection 
# Sort 
 
arr = [64, 25, 12, 22, 11] 

  
# Traverse through all array elements 
def sort(arr):
    for i in range(len(arr)): 
          
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i + 1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
                  
        # Swap the found minimum element with  
        # the first element         
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 

        
arr = [64, 25, 12, 22, 11]
print(arr);        
sort(arr)
print(arr);
