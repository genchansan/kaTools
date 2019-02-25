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
    xformClr = hou.Color((0.29,0.565,0.886))

    #for now
    shapes = ['rect', 'bone', 'bulge', 'bulge_down', 'burst', 'camera', 'chevron_down', 'chevron_up',
     'cigar', 'circle', 'clipped_left', 'clipped_right', 'cloud', 'diamond', 'ensign',
      'gurgle', 'light', 'null', 'oval', 'peanut', 'pointy', 'slash', 'squared', 'star',
       'tabbed_left', 'tabbed_right', 'task', 'tilted', 'trapezoid_down', 'trapezoid_up', 'wave']

    clrSet = [["attribwrangle",wrangleClr],["volumewrangle",wrangleClr],
    ["solver",dopClr],["dopnet",dopClr, 'burst'],
    ["object_merge",objMergeClr],["attribvop",vopClr],["volumevop",vopClr],
    ["subnet",subnetClr],["xform", xformClr, "slash"]]
    
    ### for AL
    clrSet.extend([["cachewrite",sopRopClr],["cacheread",sopRopClr]])
    ### for IE
    clrSet.append(["ieSopReader",sopRopClr])



    

    #######################
    currentNodes = hou.selectedNodes()
    
    for node in currentNodes:
        #print node.type().name()
        for eachClr in clrSet:
            if node.type().name() == eachClr[0]:
                node.setColor(eachClr[1])
                if len(eachClr)>2:
                    node.setUserData('nodeshape', eachClr[2])

        if node.type().name() == "geo":
            if node.name().find("FX") != -1:
                node.setColor(geoFxClr)
            elif node.name().find("REN") != -1:
                node.setColor(geoRenClr)
            else:
                node.setColor(geoClr)
