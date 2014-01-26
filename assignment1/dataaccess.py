from models import Node

def getNodes():
	q = Node.query()
	nodes = q.fetch(100)
	return nodes

def setNode(stub, raddr):
	fChar = stub[:1]
	if fChar.isalpha():
		fChar = fChar.lower()
	else:
		fChar = "else"

	a = Node(stub = stub, remoteaddrs = raddr, f = fChar)
	a.put()