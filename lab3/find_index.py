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
    def find_index(self, n):
        curr = self.head
        if self.head == None:
            print("Error")
            return
        i = 0
        while (i<n - 1 and curr.next != None):
            # print(curr.data)
            curr = curr.next
            i+=1
        if (i != n - 1):
            print("Error")
        else:
            print(curr.data)
class DataNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None
def main():
    listed = SinglyLinkedList()
    while (True):
        text = input()
        if text == 'Last':
            break
        listed.insert_last(text)
    listed.find_index(int(input()))
main()
