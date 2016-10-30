import hou
import math

limit = len(hou.selectedNodes())
yPos = []

for aNode in hou.selectedNodes():
    yPos.append([aNode.position()[1], aNode])
    yPos = sorted(yPos)

for i in xrange(len(yPos) - 1):
    yPos[i][1].setInput(0,yPos[i+1][1])

for yNode in hou.selectedNodes():
    yFit = math.floor(yNode.position()[0])
    mean = (yNode.position()[1]) - (yFit) / (limit)
