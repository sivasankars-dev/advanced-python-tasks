class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            curr = self.head
            while curr.pointer is not None:
                curr = curr.pointer

            curr.pointer = newnode

    def remove(self, data):
        if self.head is not None:
            if self.head.data == data:
                self.head = self.head.pointer
            else:
                curr = self.head
                while curr.pointer is not None and curr.pointer.data != data:
                    curr = curr.pointer
                
                if curr.pointer is not None:
                    curr.pointer = curr.pointer.pointer
                else:
                    print(f"{data} is not in linkedlist")
        else:
            print(f"You can't remove at empty linkedlist")

    def search(self, data):
        if self.head is not None:
            curr = self.head
            while curr.pointer is not None:
                if curr.data == data:
                    print(f'{data} is exist')
                    return
                curr = curr.pointer
            print(f'{data} is not exist')
        else:
            print(f"Your linkedlist is empty. you can't search")

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.pointer

l1 = Linkedlist()
l1.add(10)
l1.add(20)
l1.add(30)
l1.add(40)
l1.show()
l1.remove(10)
print("After Removed 10")
l1.show()
print()
l1.search(10)
