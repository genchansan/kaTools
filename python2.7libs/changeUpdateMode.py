import hou

def execute():
    if hou.ui.updateMode() == hou.updateMode.AutoUpdate :
        hou.setUpdateMode(hou.updateMode.Manual)
    else:
        hou.setUpdateMode(hou.updateMode.AutoUpdate)
        hou.ui.triggerUpdate()
