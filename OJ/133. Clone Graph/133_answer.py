# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def createNode(self, oldNode):
        newNode = UndirectedGraphNode(oldNode.label)
        self.newNodeDict[newNode.label] = newNode
        for i in oldNode.neighbors:
            if i.label not in self.newNodeDict:
                self.createNode(i)
            newNode.neighbors.append(self.newNodeDict[i.label])
        return newNode
        
    def cloneGraph(self, node):
        if not node:
            return None
        self.newNodeDict = {}
        return self.createNode(node)


        


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    node0 = UndirectedGraphNode(0)
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    node0.neighbors = [node1, node2]
    node1.neighbors = [node2]
    node2.neighbors = [node2]
    print s.cloneGraph(node0).label
    finish = clock()
    print (finish - start) * 1000