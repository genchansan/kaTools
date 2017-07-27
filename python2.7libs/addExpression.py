# -*- coding: utf-8 -*-
import hou
import xml.etree.ElementTree as ET
import sys
import xml.parsers.expat as ep
import lxml.etree as let


class wranglePreset:

	parser = ""
	menus = []
	inSet=False
	inExp=False
	expression=''

	#makeMenus = 0
	#paste = 1
	#saveXML = 2
	#deleteXML = 3
	def __init__(self, mode, kwargs=None):
		self.XMLPath = hou.expandString("$HOUDINI_PATH").split(";")[-2] + '/expressions.xml'
		self.tree = ET.parse(self.XMLPath)

		parser = let.XMLParser(resolve_entities=False, remove_blank_text=True, strip_cdata=False)
		self.tree2 = let.parse(self.XMLPath, parser)
		self.kwargs = kwargs

		self.parser = ep.ParserCreate("UTF-8")
		if mode == 0:
			#self.parser.CharacterDataHandler = self.handleCharData
			self.parser.StartElementHandler = self.handleStartElementMakeMenus
			#self.parser.EndElementHandler = self.handleEndElement

		if mode == 1:
			self.parser.CharacterDataHandler = self.handleCharElementPasteExpression
			self.parser.StartElementHandler = self.handleStartElementPasteExpression
			self.parser.EndElementHandler = self.handleEndElementPasteExpression




	def handleCharElementPasteExpression(self, data):
		if self.inExp == True and self.inSet == True:
			print 'Character data:', data
			if data != "\t" and data != "\n":
				self.expression += data

	def handleStartElementPasteExpression(self, name, attrs):
		if name == "set":
			print 'Start element:', name, attrs['name'], self.kwargs["selectedlabel"]
			if self.kwargs["selectedlabel"] == attrs['name']:
				if self.inSet==False:
					self.inSet = True
				#elif self.inSet==True:
					#self.inSet = False
				#print self.inExp, self.inSet
		if name == "expression":
			print 'Start element:', name, attrs
			if self.inExp==False:
				self.inExp = True
			#elif self.inExp==True:
				#self.inExp = False
			#print self.inExp, self.inSet

	def handleEndElementPasteExpression(self, name):
		if name == "set":
			print 'End element:', name
			if self.inSet==True:
				self.inSet = False
			#print self.inExp, self.inSet
		if name == "expression":
			print 'End element:', name
			if self.inExp==True:
				self.inExp = False
			#print self.inExp, self.inSet



	def handleStartElementMakeMenus(self, name, attrs):
		if name == "set":
			self.menus.append(attrs["name"])
			self.menus.append(attrs["name"])
			#print 'Start element:', name, attrs
	def handleEndElement(self, name):
		print 'End element:', name



###########################################################################







	def paste(self, kwargs):

		#self.parser.ParseFile(open(self.XMLPath, "r"))

		root = self.tree2.getroot()
		expression = root.find("./set[@name='" + kwargs["selectedlabel"] +"']").find('expression').text
		
		kwargs["parms"][0].set(kwargs["parms"][0].eval() + expression)





	def makeMenus(self):
		
		root = self.tree2.getroot()
		
		for menuset in root:
			self.menus.append(menuset.attrib[("name")])
			self.menus.append(menuset.attrib[("name")])
		
		#self.parser.ParseFile(open(self.XMLPath, "r"))

		return self.menus


	def saveXML(self,kwargs):
		root = self.tree2.getroot()

		accept, name = hou.ui.readInput("Preset Name:", buttons=('OK','Cancel'), close_choice=1)
		if accept == 1:
			return

		expression = kwargs["parms"][0].eval()
		#expression = "\n<![CDATA[%s]]>\n" % expression
		expression = let.CDATA(expression)

		setElement = let.Element("set")
		setElement.set("name", name)
		expressionElement = let.Element("expression")
		expressionElement.text = expression
		root.append(setElement)
		setElement.append(expressionElement)

		#self.tree.write(self.XMLPath, "utf-8", True)
		self.tree2.write(self.XMLPath, encoding="utf-8", method="xml", pretty_print = True)

