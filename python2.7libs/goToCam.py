import hou

def execute():
    viewports = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
    viewports.curViewport().setCamera(hou.node("/obj/renderCamera"))



def executeAL():
    viewports = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
    cam = find()
    if cam is not None:
        viewports.curViewport().setCamera(cam)
    else:
        cam = findOther()
        if cam is not None:
            viewports.curViewport().setCamera(cam)



def find():
    obj = hou.node("/obj")
    camObj = obj.glob("*camera*")
    cam = None
    if len(camObj)>0:
		cam = hou.node(camObj[0].path() + "/left")

    return cam

def findOther():
    obj = hou.node("/obj")
    camObj = obj.recursiveGlob("*", hou.nodeTypeFilter.ObjCamera)

    cam = None
    if camObj != None:
		cam = camObj[0]

    return cam