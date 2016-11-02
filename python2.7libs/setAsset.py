import hou
import xml.etree.ElementTree as ET

def execute():
    obj = hou.node("/obj")
    home = hou.expandString("$HOME")
    
    tree = ET.parse( home +'/houdini15.5/kaTools/python2.7libs/extractAsset.xml')
    root = tree.getroot()
    
    for child in root:
        targetNode = obj.glob(child.attrib["name"])
        print targetNode
        if targetNode != ():
            print child.tag, child.attrib
            for element in child:
                targetNode[0].parm(element.tag).set(element.text)
                print element.tag, element.text
