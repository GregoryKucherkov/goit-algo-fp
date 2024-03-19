#Linked list 
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self, *args):
        self.head = None
        for data in args:
            self.insert(data)

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    #reversal function
    def reversal(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print('End')

# sort function
def insertion_sort(lst):
    sorted_list = None
    current = lst.head
    while current != None:
        next = current.next
        sorted_list = sortedInsert(sorted_list, current)
        current = next

    lst.head = sorted_list
    return lst

def sortedInsert(lst, new_node):
    current = None
    if lst == None or lst.data >= new_node.data:
        new_node.next = lst
        lst = new_node
    else:
        current = lst
        while current.next != None and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        
    return lst

# merge function
def merge(list_1, list_2):
    if not list_2:
        return list_1
    elif not list_1:
        return list_2
    
    current = list_1.head
    while current.next:
        current = current.next
    current.next = list_2.head

    merged = insertion_sort(list_1)
    return merged
 

#Usage
if __name__ == "__main__":
    llist_1 = Linkedlist(5, 68, 32, 45, 67, 21)
    llist_2 = Linkedlist(6, 65, 76, 34, 98, 45)

    print("Original list  1:")
    llist_1.print_list()

    print("\nReversed list 1:")
    llist_1.reversal()
    llist_1.print_list()

    print("\nSorted lists:")
    insertion_sort(llist_1).print_list()
    insertion_sort(llist_2).print_list()

    print("\nMerged 2 sorted lists:")
    result = merge(llist_1, llist_2)
    result.print_list()

