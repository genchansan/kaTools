import hou

def paste(kwargs):

    tree = ET.parse(hou.expandString("$HOUDINI_PATH").split(";")[0] + '/expressions.xml')
    root = tree.getroot()
    expression = root.find("./set[@name='" + kwargs["selectedlabel"] +"']").find('expression').text

    #print kwargs["selectedtoken"]
    #print kwargs["selectedlabel"]
    #print kwargs["parms"][0]

    kwargs["parms"][0].set(kwargs["parms"][0].eval() + expression)

    return expression


###########################################################################

import xml.etree.ElementTree as ET

def readXML():
    tree = ET.parse(hou.expandString("$HOUDINI_PATH").split(";")[0] + '/expressions.xml')
    root = tree.getroot()
    menus = []
    for menuset in root:
        menus.append(menuset.tag)
        menus.append(menuset.attrib[("name")])

    return menus