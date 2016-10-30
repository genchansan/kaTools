import hou

def execute():
    viewports = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
    viewports.curViewport().setCamera(hou.node("/obj/renderCamera"))
