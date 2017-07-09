import hou

def absToRel(kwargs):
    parm = kwargs["parms"][0]
    origNode = parm.node()
    refNode = hou.node(parm.eval())

    pathlist = parm.eval().split("/")

    if pathlist[0] == "..":
        return

    relNode = origNode.relativePathTo(refNode)
    parm.set(relNode)




def relToAbs(kwargs):
    parm = kwargs["parms"][0]
    origNode = parm.node()

    pathlist = parm.eval().split("/")

    if pathlist[0] != "..":
        return

    parent = origNode
    restPath = ""
    length = len(pathlist)

    for i in range(0,length):
        part = pathlist[i]
        if part == "..":
            parent = parent.parent()
            #print parent.path()
        else:
            restPath += "/" + part

    if hou.node(parent.path() + restPath) != None:
        parm.set(parent.path() + restPath)
    #else:
        #print "maybe wrong path"