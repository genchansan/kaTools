# -*- coding: utf-8 -*-
import hou
import xml.etree.ElementTree as ET

class wranglePreset:
    def __init__(self):
        self.XMLPath = hou.expandString("$HOUDINI_PATH").split(";")[-2] + '/expressions.xml'
        self.tree = ET.parse(XMLPath)


        

    def paste(kwargs):

	#self.tree = ET.parse(hou.expandString("$HOUDINI_PATH").split(";")[-2] + '/expressions.xml')
	root = self.tree.getroot()
	expression = root.find("./set[@name='" + kwargs["selectedlabel"] +"']").find('expression').text

	#print kwargs["selectedtoken"]
	#print kwargs["selectedlabel"]
	#print kwargs["parms"][0]

	print kwargs

	kwargs["parms"][0].set(kwargs["parms"][0].eval() + expression)

	return expression



###########################################################################



    def readXML():
	#tree = ET.parse(hou.expandString("$HOUDINI_PATH").split(";")[-2] + '/expressions.xml')
	root = self.tree.getroot()
	menus = []
	for menuset in root:
	    menus.append(menuset.tag)
	    menus.append(menuset.attrib[("name")])

	return menus


    def saveXML(kwargs):
	#XMLPath = hou.expandString("$HOUDINI_PATH").split(";")[-2] + '/expressions.xml'
	#tree = ET.parse(XMLPath)
	root = self.tree.getroot()

	accept, name = hou.ui.readInput("Preset Name:")
	expression = kwargs["parms"][0].eval()

	setElement = ET.Element("set")
	setElement.set("name", name)
	expressionElement = ET.Element("expression")
	expressionElement.text = expression
	root.append(setElement)
	setElement.append(expressionElement)


	tree.write(XMLPath, "UTF-8", True)
    
