def execute():
    wrangleClr = hou.Color((1,0.8,0.0))
    sopRopClr = hou.Color((0.4,1,0.4))
    dopClr = hou.Color((0.4,1,1))
    vopClr = hou.Color((1,1,0.6))
    objMergeClr = hou.Color((0,0.6,1))
    nullClr = hou.Color((0.6,0.6,1))
    
    #######################
    currentNode = hou.selectedNodes()
    
    for node in currentNode:
        print node.type().name()
        if node.type().name() == "attribwrangle":
            node.setColor(wrangleClr)
        elif node.type().name() == "volumewrangle":
            node.setColor(wrangleClr)   
        elif node.type().name() == "ieSopRop":
            node.setColor(sopRopClr)
        elif node.type().name() == "ieSopReader":
            node.setColor(sopRopClr)
        elif node.type().name() == "solver":
            node.setColor(dopClr)
        elif node.type().name() == "dopnet":
            node.setColor(dopClr)
        elif node.type().name() == "object_merge":
            node.setColor(objMergeClr)
        elif node.type().name() == "null":
     
