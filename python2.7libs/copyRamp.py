import hou

####################################
def checkRamps(node):
    rampList=[]
    for parm in node.parms():
        try:
            parm.evalAsRamp()
            rampList.append(parm)
            #print parm.name()
        except TypeError:
            name = parm.name()
            #print "not" + name
    return rampList
####################################s
def selectRamp(rampList):
    names = []
    count = 0
    for ramp in rampList:
        names.append( ramp.name())
    
    return hou.ui.selectFromList(names, default_choices = (0,))

####################################

def execute():
    selected = hou.selectedNodes()
    if len(selected)==2:

        origNode = hou.selectedNodes()[0]
        destNode = hou.selectedNodes()[1]

        origRamps = []
        destRamps = []

        origRamps = checkRamps(origNode)
        destRamps = checkRamps(destNode)

        origRamp =  origRamps[selectRamp(origRamps)[0]]
        destRamp =  destRamps[selectRamp(destRamps)[0]]


        ramp = origRamp.evalAsRamp()
        basis = ramp.basis()
        keys = ramp.keys()
        values = ramp.values()

        #print destRamp
        if ramp.isColor() is destRamp.evalAsRamp().isColor():
            destRamp.set( hou.Ramp(basis,keys,values))
        else:
            hou.ui.displayMessage("different type")


    else:
        print hou.ui.displayMessage("select 2 nodes")
