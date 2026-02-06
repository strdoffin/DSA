class BSTNode:
    def __init__(self, data: int = None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
            return
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = BSTNode(data)
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = BSTNode(data)
                        break
    def preorder(self):
        self._preorder(self.root)

    def _preorder(self,node):
        if node is None:
            return
        if node.data is not None:
            print("->", node.data, end=" ")
        if node.left:
            self._preorder(node.left)
        if node.right:
            self._preorder(node.right)

def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
    
  print("Preorder: ", end="")
  my_bst.preorder()

main()
