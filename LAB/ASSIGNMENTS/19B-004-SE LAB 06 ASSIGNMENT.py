# MUHAMMAD OMER SIDDIQUI
# 19B-004-SE DSA LAB 06 ASSIGNMENT
# ================XXXXXX================== #
# PART A
#converting singly linkedlist to doubly linkedlist
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

# ================XXXXXX================== #
        
class DoublylinkedList:
    def __init__(self):
        self.start_node = None
            
# ================XXXXXX================== #
    def InsertAtFirst(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return 
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node
        return "Inserting item in Doubly Linkedlist is :{}".format(data)
        

# ================XXXXXX================== #
    def InsertAtEnd(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        end = self.start_node
        while end.next is not None:
            end = end.next
        new_node = Node(data)
        end.next = new_node
        new_node.prev = end
        return "Inserting item at the end in Doubly Linkedlist is :{}".format(data)
# ================XXXXXX================== #
    def InsertAfter(self, item, data):
        if self.start_node is None:
            return "element not found"
        else:
            val = self.start_node
            while val is not None:
                if val.item == item:
                    break
                val = val.next
            if val is None:
                return "element not found"
            else:
                new_node = Node(data)
                new_node.prev = val
                new_node.next = val.next
                if val.next is not None:
                    val.next.prerev = new_node
                val.next = new_node
        return "Inserting {} after {} in Doubly Linkedlist".format(item,data)
        
                
# ================XXXXXX================== #
    def DeleteAtFirst(self):
        if self.start_node is None:
            return "element not found"
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next


        

# ================XXXXXX================== #
    def DeleteAtEnd(self):
        if self.start_node is None:
            return "element not found" 
        if self.start_node.next is None:
            self.start_node = None
            return
        end_val = self.start_node
        while end_val.next is not None:
            end_val = end_val.next
        end_val.prev.next = None

# ================XXXXXX================== #        
    def DeletebyValue(self, val):
        if self.start_node is None:
            return "element not found"
        if self.start_node.next is None:
            if self.start_node.item == val:
                self.start_node = None
            else:
                return "element not found"
            return 

        if self.start_node.item == val:
            self.start_node = self.start_node.next
            self.start_node.prev = None
            return
        temp = self.start_node
        while temp.next is not None:
            if temp.item == val:
                break
            temp = temp.next
        if temp.next is not None:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        else:
            if temp.item == val:
                temp.prev.next = None
            else:
                return "element not found"

# ================XXXXXX================== #
    def Print(self):
        y=self.start_node
        while y:
            print( "Item in Doubly Linkedlist is {}".format(y.item))
            y=y.next

        
                
#DRIVER CODE              
# object = DoublylinkedList()
# print(object.InsertAtFirst(50))
# print(object.InsertAtFirst(20))
# print(object.InsertAtFirst(30))
# print(object.InsertAtEnd(29))
# print(object.InsertAtEnd(39))
# print(object.InsertAtEnd(49))
# object.DeleteAtFirst()
# object.DeleteAtEnd()
# object.DeletebyValue(29)
# print(object.InsertAfter(50, 1))
# object.Print()