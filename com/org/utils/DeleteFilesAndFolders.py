'''
Created on Dec 30, 2018

@author: penumr
'''
import os
import time;


def delete(folder):
    fileList = os.listdir(folder)
    if(len(fileList) == 0):
        try:
            os.rmdir(folder)
        except:
            pass
    for f in fileList:
        if('python' in f):
            continue
        
        filePath = folder + '/' + f
    
        if os.path.isfile(filePath):
            try:
                os.remove(filePath)
                print(filePath)
            except:
                pass
    
        elif os.path.isdir(filePath):
            delete(filePath)


if __name__ == '__main__':
    folder = 'C:/Users/penumr/AppData/Local/Temp'
    delete(folder)
