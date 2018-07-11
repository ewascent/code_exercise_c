from urllib.request import urlopen
from xml.dom import minidom
from xml.dom.minidom import parse, parseString

def fetchData(xmlDoc):
    httpsock = urlopen(xmlDoc)
    data = parse(httpsock)
    httpsock.close()
    return data.toxml()

def printNodes(nodeList):
    nodes = []
    for node in nodeList:
        if node.nodeType == node.TEXT_NODE:
            nodes.append(node.data)
    return ''.join(nodes)

def getText(xmlDoc):
    docText = parseString(xmlDoc)
    titles = docText.getElementsByTagName("title")
    for title in titles:
        print("<title>%s</title>" % printNodes(title.childNodes))

getText(fetchData('http://slashdot.org/slashdot.rdf')) 
