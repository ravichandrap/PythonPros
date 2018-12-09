'''
Created on Dec 9, 2018

@author: penumr
'''


def printCountRec(distance):
    if distance < 0:
        return 0;
    if distance == 0:
        return 1;
    
    return (printCountRec(distance - 1) + printCountRec(distance - 2) + printCountRec(distance - 3));


def printCount(dist):
    count = [0] * (dist + 1)
    
    count[0] = 1;
    count[1] = 1;
    count[2] = 2;
    
    for i in range(3, dist + 1):
        count[i] = (count[i - 1] + count[i - 2] + count[i - 3]);
        
    return count[dist];


distance = 4;
print(printCountRec(distance))
print(printCount(distance))
    
