from models import Node

def getNodes():
	q = Node.query()
	nodes = q.fetch(100)
	return nodes

def setNode(stub, raddr):
        a = Node(stub = stub, remoteaddrs = raddr)
        a.put()