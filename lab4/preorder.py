class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data is None:
            self.data = data
            return
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                pNew = BSTNode(data)
                self.left = pNew
        elif data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                pNew = BSTNode(data)
                self.right = pNew
    def preorder(self):
        if self.data:
            print("->",self.data, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
def main():
    my_bst = BSTNode()
    for i in range(int(input())):
        my_bst.insert(int(input()))
    print("Preorder: ", end="")
    my_bst.preorder()

main()
