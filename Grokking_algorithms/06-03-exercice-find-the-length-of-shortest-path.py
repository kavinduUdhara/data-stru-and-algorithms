from collections import deque

graph = {}
graph["s"] = ["n1", "n2"]
graph["n1"] = ["f", "n3"]
graph["n2"] = ["n3", "n4"]
graph["n4"] = ["f"]

def getShortestPath():
    queue = deque([(0, "s", ["s"])])
    checked = set()
    while queue:
        dis, node, root = queue.popleft()
        if node not in checked:
            if node == "f":
                print(f"shortest path: {root} with {dis} steps distance.")
                return True
            else:
                checked.add(node)
                queue += [(dis + 1, subNode, root + [subNode]) for subNode in graph[node]]
    return False

getShortestPath()
