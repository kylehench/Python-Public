import os, sys
pythonPath = os.environ['USERPROFILE']+ r'\desktop\python'

def spacesPresent(item):
    #function that checks if a space is present in any list or multi-level list
    for lowerItem in item:
        if isinstance(lowerItem, list):
            if spacesPresent(lowerItem):
                return True
        elif isinstance(lowerItem, str):
            if ' ' in lowerItem:
                return True
    return False

def createNewDirs(startingDir,newDirs):
    for l in newDirs:
        middle = l[0]
        os.mkdir(pythonPath + '\\' + middle)
        for newDir in l[1:]:
            os.mkdir(pythonPath + '\\' + middle + '\\' + newDir)
    
if os.path.exists(pythonPath):
    #createNewDirs(1,2)
    folderList = [['ajax','ajax_api','ajax_flask'],
                  ['flask','fundamentals'],
                  ['flask_mysql','belt_review','crud','db_connection','validation'],
                  ['fundamentals','extras','fundamentals','introduction','oop'],
                  ['mysql','erd','queries']]
    if spacesPresent(folderList):
        sys.exit()
    createNewDirs(pythonPath,folderList)
