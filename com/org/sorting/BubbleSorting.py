'''
Created on Nov 29, 2018

@author: penumr
'''


def bubbleSortNormal(arr): 
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubbleSortOptimized(arr):
    n = len(arr);
    swapped = False;
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if swapped == False:
            break;

    
arr = [64, 34, 25, 12, 22, 11, 90] 
arr2 = [64, 34, 25, 12, 22, 11, 90] 
print(arr)
bubbleSortNormal(arr);
print(arr)
print("----------")
print(arr2)
bubbleSortOptimized(arr2)
print(arr2)
