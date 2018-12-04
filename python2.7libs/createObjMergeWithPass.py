# -*- coding: utf-8 -*-

import hou
def execute():

	editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
	#print editor.pwd()
	#editor.pwd().pasteItemsFromClipboard(editor.visibleBounds().center())
	#print hou.ui.getTextFromClipboard()
	copied = hou.node(hou.ui.getTextFromClipboard())
	merge = editor.pwd().createNode("object_merge", "IN_" + copied.name())
	merge.setPosition(editor.visibleBounds().center())
	inPath = merge.parm('objpath1').set(hou.ui.getTextFromClipboard())