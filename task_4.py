import uuid
import networkx as nx
import matplotlib.pyplot as plt
import copy 

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  
        self.id = str(uuid.uuid4())  

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, traversal_order=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if traversal_order is None:
        colors = [node[1]['color'] for node in tree.nodes(data=True)]
    else:
        num_nodes = len(traversal_order)
        color_scheme = ['#001F3F', '#003366', '#004080', '#00509E', '#0066CC', '#0077B6', '#0088D4', '#0099ED',
                        '#00A8FF', '#00BBFF', '#00CCFF', '#00DDFF', '#00EEFF', '#00FFFF', '#66FFFF', '#99FFFF']
        colors = [color_scheme[i % len(color_scheme)] for i in range(num_nodes)]

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  
    
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# heapify function
def heap_b(tree_copy):
    if not tree_copy:
        return None
    
    heap_b(tree_copy.left)
    heap_b(tree_copy.right)
    
    # Compare the node's value with its children
    min_val = tree_copy.val
    min_node = tree_copy

    if tree_copy.left and tree_copy.left.val < min_val:
        min_val = tree_copy.left.val
        min_node = tree_copy.left
    
    if tree_copy.right and tree_copy.right.val < min_val:
        min_val = tree_copy.right.val
        min_node = tree_copy.right
    
    # If the minimum value is not in the current node,
    # swap the values and recursively heapify the affected subtree
    if min_node != tree_copy:
        tree_copy.val, min_node.val = min_node.val, tree_copy.val
        heap_b(min_node)  # Recursively heapify the affected subtree

    return tree_copy


# Створення дерева
root = Node(4)
root.left = Node(0)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(3)
root.right.left = Node(1)

# Usage. The program shows a binary tree, then it rebuild it to the heap, and visualize.
if __name__ == '__main__':
    # Tree display
    draw_tree(root)

    # Copy the original tree
    root_copy = copy.deepcopy(root)
    
    # Heapify the tree
    heap_b(root_copy)

    # Heapified tree display
    draw_tree(root_copy)

