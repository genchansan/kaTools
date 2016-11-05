import hou


def execute():
    selected = hou.selectedNodes()
    if len(selected)==2:
		origParentNode = hou.selectedNodes()[0]
		destParentNode = hou.selectedNodes()[1]

		

		allOrigNodes = origParentNode.recursiveGlob("*")
		allDestNodes = destParentNode.recursiveGlob("*")

		for destNode in allDestNodes:
			pasteReference(destNode, allOrigNodes)

    else:
        print hou.ui.displayMessage("select 2 nodes")



def pasteReference(destNode, allOrigNodes):
	targetOrigNode = findTarget(destNode, allOrigNodes)
	if targetOrigNode == None:
		return

	relPath = destNode.relativePathTo(targetOrigNode)

	for destParm in destNode.parms():
		for targetOrigNodeParm in targetOrigNode.parms():
			if destParm.name() == targetOrigNodeParm.name():
				setParm(destParm, targetOrigNodeParm, relPath)
				break



def findTarget(destNode, allOrigNodes):
	for origNode in allOrigNodes:
		if origNode.name() == destNode.name():
			if origNode.type().name() == destNode.type().name():
				return origNode
	return None





def setParm(destParm, targetOrigNodeParm, relPath):
	parmType = destParm.parmTemplate().type()
	if parmType == hou.parmTemplateType.Int or parmType == hou.parmTemplateType.Float \
	or parmType == hou.parmTemplateType.Toggle or parmType == hou.parmTemplateType.Menu or parmType == hou.parmTemplateType.Button \
	or parmType == hou.parmTemplateType.Ramp:
		#or parmType == hou.parmTemplateType.FolderSet or parmType == hou.parmTemplateType.Folder
		destParm.deleteAllKeyframes()
		destParm.setExpression('ch("' + relPath +"/"+ targetOrigNodeParm.name() + '")')

	elif parmType == hou.parmTemplateType.String:
		destParm.deleteAllKeyframes()
		destParm.set('`chs("' + relPath + "/" + targetOrigNodeParm.name() + '")`')
