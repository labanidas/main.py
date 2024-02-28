class node:
    def _init_(self,value):
        self.data = value
        self.next = None
        
class linkedlist:
    def _init_(self):
        self.head = None
        self.n = 0
        
    def _len_(self):
        return self.n
        
    def insert_head(self,value):
        new_node = node(value)
        new_node.next = self.head
        self.head = new_node
        self.n = self.n + 1
        
    def _str_(self):
        curr = self.head
        result = ""
        while curr != None:
            result = result + str(curr.data) + "->"
            curr = curr.next
        return result[:-2]
        
    def append(self,value):
        new_node = node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n = self.n + 1
        
    def insertmiddle(self,element,value):
        new_node = node(value)
        curr = self.head
        while curr != None:
            if curr.data == element:
                break
            curr = curr.next
        if curr == None:
            print(f"{element} is not present in Linkedlist.")
            return
        new_node.next = curr.next
        curr.next = new_node
        self.n = self.n + 1
               
    def clear(self):
        self.head = None
        self.n = 0
              
    def delete_head(self):
        if self.head == None:
            print("Linkedlist is empty.")
            return
        self.head = self.head.next
        self.n -= 1
        
    def pop(self):
        if self.head == None:
            print("Linkedlist is empty.")
            return
        if self.head.next == None:
            self.delete_head()
            return
        curr = self.head
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n -= 1
        
    def delete_middle(self,element):
        if self.head == None:
            print("Linkedlist is empty.")
            return
        if self.head.data == element:
            self.delete_head()
            return
        else:
            if self.head.next == None:
                print(f"{element} is not present in Linkedlist.")
                return
        curr = self.head
        while curr.next.next != None:
            if curr.next.data == element:
                break
            curr = curr.next
            
        if curr.next.next == None:
            if curr.next.data == element:
                self.pop()
                return
            else:
                print(f"{element} is not present in Linkedlist.")
                return
        curr.next = curr.next.next
        self.n -= 1
            
        
l = linkedlist()
