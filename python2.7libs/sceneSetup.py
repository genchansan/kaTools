#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import glob
import imghdr
import hou



'''
sort functions
'''

def getFrameNum(iterFile):
    num = re.findall(r'\d+', iterFile)
    if len(num) >0:
        print num[-1]
        return num[-1]
    else:
        print iterFile[0]
        return iterFile[0]






'''
set up project
'''

def selectProjectDir(projpaths):
    projDir = None
    if len(projpaths)>0:
        choices = hou.ui.selectFromList(projpaths)
        if choices is ():
            pass
        else:
            projDir = projpaths[choices[0]]
            if projDir is not None:
                print "set variable PROJECTDIR to", projDir
                hou.hscript("setenv 'PROJECTDIR'=" + projDir)
    return projDir
                


    
'''
set up shot
'''

def selectShot(shots):
    shot = None
    if len(shots)>0:
        shots = sorted(shots)
        choices = hou.ui.selectFromList(shots)
        if choices is ():
            pass
        else:
            shot = shots[choices[0]]
            if shot is not None:
                print "set variable SHOT to", shot
                hou.hscript("setenv 'SHOT'=" + shot)
    return shot



def createTemplateDirs(shotDir):
    print "create template dirs in ", shotDir
    dirs = ["ae", "geo/cache", "hip", "out", "ref", "ren/comp", "plate", "nk"]
    for dirToCreate in dirs:
        targetPath = os.path.join(shotDir, dirToCreate)
        exist = os.path.exists(targetPath)
        if exist == True:
            print dirToCreate, " exists."
        else:
            try:
                os.makedirs(targetPath)
                print dirToCreate, "created."
            except OSError:
                print OSError
                print "had a trouble with creating", targetPath



'''
set up frame range
'''
 

def getSeqInfoFromFile(file):
    dir = os.path.dirname(file)
    file = os.path.basename(file)
    segNum = re.findall(r'\d+', file)[-1]
    numPad = len(segNum)

    baseName = file.split(segNum)[0]
    fileType = file.split('.')[-1]
    globString = baseName
    for i in range(0,numPad): 
        globString += '?'
    theGlob = glob.glob(dir+'/'+globString+file.split(segNum)[1])
    numFrames = len(theGlob)
    if numFrames == 0:
        return None
    theGlob = sorted(theGlob, key=getFrameNum)
    
    firstFrame = theGlob[0]
    lastFrame = theGlob[-1]
    return [baseName, numPad, fileType, numFrames, firstFrame, lastFrame]
 
 
def getSeqInfoUnderDir(plateDir):
    if os.path.exists(plateDir) is not True:
        print "no folder"
        return None, None, None
    imageFiles = os.listdir(plateDir)
    if len(imageFiles) == 0:
        print "no files"
        return None, None, None
    for iterFile in imageFiles:
        what= imghdr.what(os.path.join(plateDir, iterFile))
        if what is None:
            imageFiles.remove(iterFile)
        
    # sort by frame order
    imageFiles = sorted(imageFiles, key=getFrameNum)
    
    firstFrame = int(re.findall(r'\d+', imageFiles[0])[-1])
    lastFrame = int(re.findall(r'\d+', imageFiles[-1])[-1])
    duration = len(imageFiles)
    
    return firstFrame, lastFrame, duration
 

def setFrameRange(firstFrame, lastFrame):
    if firstFrame is None or lastFrame is None:
        return False
    else:
        currentRange = hou.playbar.frameRange()
        hou.playbar.setFrameRange(firstFrame, lastFrame)
        hou.hscript("setenv SHOTSTART = " + str(firstFrame))
        print "set $SHOTSTART to", str(firstFrame)
        hou.hscript("setenv SHOTEND = " + str(lastFrame))
        print "set $SHOTEND to", str(lastFrame)
        if firstFrame > currentRange[1] or lastFrame < currentRange[0]:
            hou.playbar.setPlaybackRange(firstFrame, lastFrame)
        return True


def setFrameRangeFromPlate(dir=None):
    #print getSeqInfoFromFile(dir) # dir should be actually a file path

    if dir is not None:
        firstFrame, lastFrame, duration = getSeqInfoUnderDir(dir)
        setFrameRange(firstFrame, lastFrame)




'''
set up all
'''

def setProject():
    file = "/promethium/init/projectDir.txt"
    f= open(file,"r")
    fl = f.readlines()

    projpaths = []

    for line in fl:
        projpath = line.split("=")[1].rstrip().replace("\"", "")
        print projpath
        exist = os.path.exists(projpath)
        
        if exist != True:
            print "This project Directory doesnt exist."
            pass
        else:
            projpaths.append(projpath)
            
    projpath = selectProjectDir(projpaths)
            
    if projpath is None:
        pass
    else:
        dirs = os.listdir(projpath)
        shotDirs = []
        for dir in dirs:
            if os.path.isfile(os.path.join(projpath,dir)):
                #print dir, "is a file"
                continue
            if re.search("^c\d", dir) != None or re.search("assets", dir) != None:
                shotDirs.append(dir)
                
        shot = selectShot(shotDirs)
        if shot is None:
            pass
        else:
            # create template directories
            needTemplates = hou.ui.displayConfirmation("Create Template directories?")
            if needTemplates is True:
                createTemplateDirs(os.path.join(projpath, shot))
            
            # set up frame range
            needFrameRange = hou.ui.displayConfirmation("Set Frame Range?")
            if needFrameRange is True:
                plateDir = os.path.join(hou.expandString("$PROJECTDIR"), hou.expandString("$SHOT"))
                plateDir = os.path.join(plateDir, "plate")
                setFrameRangeFromPlate(plateDir)















'''
fix name
'''

def changePlateName(dir=None):
    shot = hou.expandString("$SHOT")
    projDir = hou.expandString("$PROJECTDIR")
    if shot == "" or projDir == "":
        print "not valid path1"
        return None
    dir = os.path.join(projDir, shot)
    dir = os.path.join(dir, "plate")

    if dir is None or os.path.exists(dir) is not True:
        print "not valid path2"
        return None

    imageFiles = os.listdir(dir)
    imageFiles = sorted(imageFiles, key=getFrameNum)

    for eachfile in imageFiles:
        newName = re.findall(r'\d+', eachfile)[-1]
        newName = shot + "_plate_" + newName + eachfile.split(newName)[-1]

        os.rename(os.path.join(dir, eachfile), os.path.join(dir, newName))