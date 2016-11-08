import hou


def execute():

    selectedNodes = hou.selectedNodes()

    for node in selectedNodes:
        for connection in node.outputConnections():
            print connection
            outputNode = connection.outputNode()
            inputIndex = connection.inputIndex()
            print outputNode.name(), inputIndex

            outputNode.setInput(inputIndex, None)
