import hou

sel = hou.selectedNodes()[0]

sel.setSelected(False)

ref = sel.parmsReferencingThis()

if len(ref) == 1:
    target = ref[0].node()
elif len(ref) >1:
    list = []
    for i in ref:
        list.append(i.node().path())
    path = hou.ui.selectFromList(list, message='to Jamp referencing Node')
    print path
    target = ref[path[0]].node()
else:
    target = sel

target.setSelected(True)

p = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
p.setCurrentNode(target)
p.homeToSelection()
