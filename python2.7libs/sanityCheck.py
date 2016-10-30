import hou

def allSubChildren(node):
    yield node
    for child_node in node.children():
        for n in allSubChildren(child_node):
            yield n

####################################

def checkErrors(node):
    warning = node.errors()
    if warning != "":
        print node.name(), "->", warning


def checkWarnings(node):
    warning = node.warnings()
    if warning != "":
        print node.name(), "->", warning


def checkMessages(node):
    warning = node.messages()
    if warning != "":
        print node.name(), "->", warning

####################################

def execute(node):
    for node in allSubChildren(node):
        checkErrors(node)
        checkWarnings(node)
        checkMessages(node)
