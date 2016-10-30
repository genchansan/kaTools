import hou
import nodeDefaultSetting

settings = nodeDefaultSetting.setting


def allSubChildren(node):
    yield node
    for child_node in node.children():
        for n in allSubChildren(child_node):
            yield n


def setUpCallback(node):
    node.addEventCallback((hou.nodeEventType.ChildCreated,), onNodeCreated)

def onNodeCreated(**kwargs):
    childNode = kwargs["child_node"]
    setUpCallback(childNode)
    #setDefaults(childNode)
    print childNode.name()


####################################

def setDefaults(node):
    for defaultSetting in settings:
        if defaultSetting["node"] == node.type().name():
            setClr(node, defaultSetting)
            setVals(node, defaultSetting)

def setClr(node, defaultSetting):
    node.setColor(hou.Color(defaultSetting["color"]))

def setVals(node, defaultSetting):
    i=0
    for parm in defaultSetting["parmnames"]:
        print parm
        node.parm(parm).set(defaultSetting["setparms"][i])
        i+=1

####################################

def execute(node):
    for eachNode in allSubChildren(node):
        eachNode.removeAllEventCallbacks()
        setUpCallback(eachNode)

    #hou.node("/").removeAllEventCallbacks()
    #hou.node("/obj").removeAllEventCallbacks()
