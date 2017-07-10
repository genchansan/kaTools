import hou

def execute():
    viewports = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
    viewports.curViewport().setCamera(hou.node("/obj/renderCamera"))



def executeAL():
    viewports = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
    cam = find()
    if cam is not None:
        viewports.curViewport().setCamera(cam)

def find():
    obj = hou.node("/obj")
    camObj = obj.glob("*camera*")
    cam = None
    if camObj != None:
		cam = hou.node(camObj[0].path() + "/left")

    return cam
