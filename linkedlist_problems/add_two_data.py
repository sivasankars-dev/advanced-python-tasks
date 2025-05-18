class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            currnode = self.head
            while currnode.pointer is not None:
                currnode = currnode.pointer
            currnode.pointer = newnode
            
    def remove(self, data):
        if self.head is not None:
            if self.head.data == data:
                self.head = self.head.pointer
            else:
                curr = self.head
                while(curr.pointer is not None and curr.pointer.data !=data):
                    curr = curr.pointer
                    
                if curr.pointer is not None:
                    curr.pointer = curr.pointer.pointer
                else:
                    print(f"{data} is not there in linkedlist")
        else:
            print("Linked is empty")
        print()
            
    def print(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.pointer
        
        
linkedlist = LinkedList()
linkedlist.add(10)
linkedlist.add(20)
linkedlist.add(30)
linkedlist.add(40)
linkedlist.print()
linkedlist.remove(20)
linkedlist.print()