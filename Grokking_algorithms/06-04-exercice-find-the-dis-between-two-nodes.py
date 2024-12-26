from collections import deque

graph = {
    "cab" : ["cat", "car"],
    "cat" : ["mat", "bat"],
    "car" : ["cat", "bar"],
    "bar" : ["bat"],
    "mat" : ["bat"],
    "bat" : []
}

def findShortestDisBetween(node1, node2):
    queue = deque()
    checked = set()
    if node1 in graph and node2 in graph:
        queue += [(node1, 0, [node1])]
        while queue:
            node, dis, root = queue.popleft()
            if node == node2:
                print(f"shortest dis. from {node1} to {node2} is: {dis}, with root: {root}")
                return True
            else:
                checked.add(node)
                queue += [(subNode, dis + 1, root + [subNode]) for subNode in graph[node]]
        return False

findShortestDisBetween("cab", "bat")