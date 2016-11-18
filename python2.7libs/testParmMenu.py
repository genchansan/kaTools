import hou

def ex(kwargs):
    parm = kwargs["parms"][0]

    referenced = parm.getReferencedParm()
    referencings = parm.parmsReferencingThis()

    if parm.node() != referenced.node():
        print "referenced : " +  referenced.name()

    referencingNodes = getNodes(referencings)

    referencingNum = selectRamp(referencingNodes)
    if len(referencingNum ) != 0:
        #print referencingNum[0]

        node = referencingNodes[referencingNum[0]]

        node.setSelected(True)

        p = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
        p.setCurrentNode(node)
        p.homeToSelection()



def selectRamp(rampList):
    names = []
    count = 0
    for ramp in rampList:
        names.append( ramp.path())
    return hou.ui.selectFromList(names, message='to Jamp referencing Node')


def getNodes(referencings):
    referencingNodes = []
    for referencing in referencings:
        referencingNodes.append(referencing.node())

    return referencingNodes
