import hou
import math


def execute():
    limit = len(hou.selectedNodes())
    yPos = []

    for aNode in hou.selectedNodes():
        yPos.append([aNode.position()[1], aNode])
        yPos = sorted(yPos)

    for i in xrange(len(yPos) - 1):
        try:
            yPos[i][1].setNextInput(yPos[i+1][1])
        except hou.Error:
            yPos[i][1].setFirstInput(yPos[i+1][1])
