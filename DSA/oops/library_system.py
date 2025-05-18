# 🔹 Task 2: Library System (Inheritance + Polymorphism)
# Requirements:
# Class hierarchy:
# Item (base class)
# Book, DVD, Magazine (inherited)
# Common attributes: title, id, is_checked_out
# Method: checkout() (override behavior in child classes)
# Stretch Goal: Use a LibraryManager to handle a collection of items using polymorphism.

class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.isCheckedOut = False

    def checkout(self):
        if not self.isCheckedOut:
            self.isCheckedOut = True
            print(f"{self.name} is checked out successfully.")
        else:
            print(f"{self.name} is already checked out")

    def checkin(self):
        if self.isCheckedOut:
            self.isCheckedOut = False
            print(f"Thank you for returning {self.name}")
        else:
            print(f"{self.name} already checked in")

class Book(Item):
    def __init__(self, id, name):
        super().__init__(id, name)

    def checkout(self):
        return super().checkout()

    def __str__(self):
        return f"Book ID is {self.id} and Book name is {self.name}"
    
class DVD(Item):
    def __init__(self, id, name):
        super().__init__(id, name)

    def checkout(self):
        return super().checkout()
    
    def __str__(self):
        return f"DVD ID is {self.id} and DVD name is {self.name}"
    
class Magazine(Item):
    def __init__(self, id, name):
        super().__init__(id, name)
    
    def checkout(self):
        return super().checkout()

    def __str__(self):
        return f"Magazine ID is {self.id} and Magazine name is {self.name}"
    
class LibraryManager:
    def __init__(self):
        self.collections = []

    def add(self, source):
        if any(existing.id == source.id for existing in self.collections):
            print(f"{source.name} is already added in the collections")           
        else: 
            self.collections.append(source)
            print(f"{source.name} is added successfully.")

    def checkout_item(self, source):
        for item in self.collections:
            if item.id == source.id:
                source.checkout()
                return          
                  
        print(f"{source.name} not found"); 
    
    def checkedin_item(self,source):
        for item in self.collections:
            if item.id == source.id:
                source.checkin()
                return
            
    def search(self, keyword):
        print(f"\nSearch Results for '{keyword}':")
        found = False
        for item in self.collections:
            if str(item.id) == str(keyword) or keyword.lower() in item.name.lower():
                print(item)
                found = True
        if not found:
            print("No matching items found.")

    def show_items(self):
        print()
        print("Existing Library Items")
        for item in self.collections:
            print(item)
    
karnanBook = Book(1, 'Name of karnan')
arjunanBook = Book(2, 'War King of arjuna')
kumutham = DVD(3, 'Weekly tamil magazine')
IITTuto = Magazine('34', 'IIT AI/ML Engineer Guidelines')

librarian = LibraryManager()
librarian.add(karnanBook)
librarian.add(karnanBook)
librarian.add(arjunanBook)
librarian.add(kumutham)
librarian.show_items()

print()
librarian.checkout_item(karnanBook)
librarian.checkout_item(karnanBook)
librarian.checkedin_item(karnanBook)

librarian.search("arjuna")
librarian.search("1")
librarian.search("nonexistent")


# Note:
# Try to implement type based search if only available. (e.g): Search only books or magazine or DVD like that




