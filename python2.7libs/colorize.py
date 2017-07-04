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

    clrSet = [["attribwrangle",wrangleClr],["volumewrangle",wrangleClr],["solver",dopClr],["dopnet",dopClr],["object_merge",objMergeClr],["attribvop",vopClr],["volumevop",vopClr],["subnet",subnetClr]]
    
    ### for AL
    clrSet.extend([["cachewrite",sopRopClr],["cacheread",sopRopClr]])
    ### for IE
    clrSet.append(["ieSopReader",sopRopClr])



    #######################
    currentNode = hou.selectedNodes()
    
    for node in currentNode:
        #print node.type().name()
        for eachClr in clrSet:
            if node.type().name() == eachClr[0]:
                node.setColor(eachClr[1])

        if node.type().name() == "geo":
            if node.name().find("FX") != -1:
                node.setColor(geoFxClr)
            elif node.name().find("REN") != -1:
                node.setColor(geoRenClr)
            else:
                node.setColor(geoClr)
