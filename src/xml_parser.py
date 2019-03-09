import io
from urllib.request import urlopen
from xml.dom.minidom import parse, parseString

async def xmlReader(xmlDoc, bufferSize=-1, seekSize=0):
    socket = io.StringIO(xmlDoc)
    socket.seek(seekSize)
    data = socket.read(bufferSize)
    socket.close()
    return data

async def fetchData(xmlDoc):
    httpsock = urlopen(xmlDoc)
    data = parse(httpsock)
    httpsock.close()
    return data.toxml()

async def printNodes(nodeList):
    nodes = []
    for node in nodeList:
        if node.nodeType == node.TEXT_NODE:
            nodes.append(node.data)
    return ''.join(nodes)

async def getText(xmlDoc):
    docText = parseString(xmlDoc)
    titles = docText.getElementsByTagName("title")
    for title in titles:
        print("<title>%s</title>" % printNodes(title.childNodes))
