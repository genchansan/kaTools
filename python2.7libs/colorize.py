import hou

def execute():
    wrangleClr = hou.Color((1,0.8,0.0))
    sopRopClr = hou.Color((0.4,1,0.4))
    dopClr = hou.Color((0.4,1,1))
    vopClr = hou.Color((1,1,0.6))
    objMergeClr = hou.Color((0,0.6,1))
    nullClr = hou.Color((0.6,0.6,1))
    subnetClr = hou.Color((0.867,0,0))
    geoClr = hou.Color((0,0.267,0))
    geoFxClr = hou.Color((0.4,1,0.4))
    geoRenClr = hou.Color((0.8,1,0.8))
    
    #######################
    currentNode = hou.selectedNodes()
    
    for node in currentNode:
        #print node.type().name()
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
            node.setColor(nullClr)
        elif node.type().name() == "attibvop":
            node.setColor(vopClr)
        elif node.type().name() == "avolumevop":
            node.setColor(vopClr)
        elif node.type().name() == "subnet":
            node.setColor(subnetClr)
        elif node.type().name() == "geo":
            if node.name().find("FX") != -1:
                node.setColor(geoFxClr)
            elif node.name().find("REN") != -1:
                node.setColor(geoRenClr)
            else:
                node.setColor(geoClr)
