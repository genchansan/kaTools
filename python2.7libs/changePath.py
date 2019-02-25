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


############################


def absToRelInExpr(node, path):

    origNode = node
    refNode = hou.node(path)
    pathlist = path.split("/")

    if pathlist[0] == "..":
        return None

    relNode = origNode.relativePathTo(refNode)
    return relNode


############################


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



############################


def relToAbsInExpr(node, path):
    origNode = node
    pathlist = path.split("/")

    if pathlist[0] ==".":
        return origNode.path()
    elif pathlist[0] != "..":
        return None

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
            if parent is not None :
                if hou.node(parent.path() + restPath) != None:
                    return parent.path() + restPath