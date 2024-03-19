from task_4 import draw_tree, root
import matplotlib
from collections import deque

def dfs(node, traversal_order=None, visited=None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []
    
    visited.add(node)
    print(f"DFS Visiting node:{node.val}") 
    traversal_order.append(node)
    
    if node.left and node.left not in visited:
        dfs(node.left, traversal_order, visited)  
    if node.right and node.right not in visited:
        dfs(node.right, traversal_order, visited)  
        
    return traversal_order


def bfs(node):
    visited_order = set()
    queue = deque([node])

    while queue:  
        vertex = queue.popleft()
        if vertex not in visited_order:
            print(f"BFS Visiting node: {vertex.val}")
            visited_order.add(vertex)
            if vertex.left:
                queue.append(vertex.left)
            if vertex.right:
                queue.append(vertex.right)
    return visited_order


if __name__ == '__main__':
    traversal_order = dfs(root)
    draw_tree(root, traversal_order)
    traversal_order_2 = bfs(root)
    draw_tree(root, traversal_order_2)

