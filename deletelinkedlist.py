class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
    def insert_last(self,data):
        new = DataNode(data)
        if self.head == None:
            self.head = new
        else:
            curr = self.head
            while (curr.next != None):
                curr = curr.next
            curr.next = new
        self.count += 1
    def traverse(self):
        curr = self.head
        if self.count == 0:
            print("This is an empty list.")
            return
        text = ""
        while (curr != None):
            text += str(curr.data) + " -> "
            curr = curr.next
        print(text.rstrip(" -> "))
    def insert_front(self,data):
        new = DataNode(data)
        if self.head == None:
            self.head = new
        else:
            end = self.head
            self.head = new
            new.next = end
        self.count += 1
    def insert_before(self, node , data):
        new = DataNode(data)
        if self.head is None:
            print("Cannot insert, "+str(node)+" does not exist.")
            return
        if self.head.data == node:
            new.next = self.head
            self.head = new
            self.count += 1
            return
        prev = None
        curr = self.head
        while (curr is not None):
            if (curr.data == node):
                prev.next = new
                new.next = curr
                self.count+=1
                return
            prev = curr
            curr = curr.next
        print("Cannot insert, "+str(node)+" does not exist.")
    def delete(self, data):
        if self.head == None:
            print("Cannot delete, "+str(data)+" does not exist.")
            return
        if self.head.data == data:
            self.head = self.head.next
            self.count -= 1
            return
        curr = self.head
        prev = None
        while (curr != None):
            if curr.data == data:
                prev.next = curr.next
                self.count -= 1
                return
            prev = curr
            curr = curr.next
        if curr is None:
            print("Cannot delete, "+str(data)+" does not exist.")
class DataNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
      mylist.insert_before(*data.split(", "))
    elif condition == "D":
      mylist.delete(data)
    else:
      print("Invalid Condition!")
  mylist.traverse()

main()