'''
Created on Nov 28, 2018

@author: penumr
'''


def search(arr, x):
    
    for i in range(len(arr)):
        if arr[i] == x:
            return i;
    return -1;


a = [2, 3, 4, 56, 7, 8, 9, 34, 66, 99]
s = 7;
print(search(a, s), a[search(a, s)])
