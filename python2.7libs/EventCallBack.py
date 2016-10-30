import hou

def setUpCallback(node):
    node.addEventCallback((hou.nodeEventType.ChildCreated,), onNodeChange)

def onNodeChange(**kwargs):
    childNode = kwargs["child_node"]
    setUpCallback(childNode)
    setClr(childNode)
    print childNode.name()

def allSubChildren(node):
    yield node
    for child_node in node.children():
        for n in allSubChildren(child_node):
            yield n

####################################

def setClr(node):
    if node.type().name() == "attribwrangle":
        attribClr = hou.Color((1.0,0.8,0))
        node.setColor(attribClr)

####################################


for node in allSubChildren(hou.node("/")):
    node.removeAllEventCallbacks()
    setUpCallback(node)
