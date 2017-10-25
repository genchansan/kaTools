import hou

def selectedParms(parms):
    names = []
    count = 0
    for parm in parms:
        names.append( parm.name())
    return hou.ui.selectFromList(names)
    
####################################

def selectedNodes(nodes):
    names = []
    count = 0
    indices = tupleAllIndices(nodes)
    for node in nodes:
        names.append( node.path())
    return hou.ui.selectFromList(names, default_choices = tuple(indices))
    
####################################

def listMatchingNodeType(baseNode, nodes):
    matches = []
    for node in nodes:
        if node.type() == baseNode.type():
            matches.append(node)
    return matches
    

####################################

def tupleAllIndices(nodes):
    num = len(nodes)
    indices = []
    for i in range(0, num):
        indices.append(i)
    return indices

####################################


def execute():
    selected = hou.selectedNodes()
    
    sourceNode = hou.selectedNodes()[0]
    
    sourceParms = sourceNode.parms()
    sourceParmsInt = selectedParms(sourceParms)
    
    if(len(sourceParmsInt)==0):
        print("No selected")
        return
    if(len(sourceParmsInt)>1):
        print("select 1 parm only")
        return
        
    sourceParm = sourceParms[sourceParmsInt[0]]
    
    root = hou.node("/obj")
    all = root.allNodes()
    
    matchNodes = listMatchingNodeType(sourceNode, all)
    
    indices = selectedNodes(matchNodes)
    if(len(indices)==0):
        print("No selected")
        return
    
    for index in indices:
        targetNode = matchNodes[index]
        targetNode.parm(sourceParm.name()).set(sourceParm.eval())
    
    
    

    