# -*- coding: utf-8 -*-
import hou
import xml.etree.ElementTree as ET
import sys
import xml.parsers.expat as ep

class wranglePreset:

	parser = ""
	menus = []

	#makeMenus = 0
	#paste = 1
	#saveXML = 2
	#deleteXML = 3
	def __init__(self, mode):
		self.XMLPath = hou.expandString("$HOUDINI_PATH").split(";")[-2] + '/expressions.xml'
		self.tree = ET.parse(self.XMLPath)

		self.parser = ep.ParserCreate("UTF-8")
		if mode == 0:
			#self.parser.CharacterDataHandler = self.handleCharData
			self.parser.StartElementHandler = self.handleStartElementMakeMenus
			#self.parser.EndElementHandler = self.handleEndElement



	def handleCharData(self, data):
		print 'Character data:', data
	def handleStartElementMakeMenus(self, name, attrs):
		if name == "set":
			self.menus.append(attrs["name"])
			self.menus.append(attrs["name"])
			print 'Start element:', name, attrs
	def handleEndElement(self, name):
		print 'End element:', name


	def paste(self,kwargs):
		root = self.tree.getroot()
		expression = root.find("./set[@name='" + kwargs["selectedlabel"] +"']").find('expression').text

		

		kwargs["parms"][0].set(kwargs["parms"][0].eval() + expression)

		return expression



###########################################################################



	def makeMenus(self):
		'''
		root = self.tree.getroot()
		menus = []
		for menuset in root:
			menus.append(menuset.attrib[("name")])
			menus.append(menuset.attrib[("name")])
		'''

		self.parser.ParseFile(open(self.XMLPath, "r"))
		self.menus

		return self.menus


	def saveXML(self,kwargs):
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

