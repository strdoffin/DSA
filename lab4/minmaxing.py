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
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self,node):
        if node is None:
            return
        if node.left:
            self._inorder(node.left)
        if node.data is not None:
            print("->", node.data, end=" ")
        if node.right:
            self._inorder(node.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self,node):
        if node is None:
            return
        if node.left:
            self._postorder(node.left)
        if node.right:
            self._postorder(node.right)
        if node.data is not None:
            print("->", node.data, end=" ")

    def traverse(self):
        if self.root is None:
            print("This is an empty binary search tree.")
            return
        print("Preorder: ",end="")
        self.preorder()
        print()
        print("Inorder: ",end="")
        self.inorder()
        print()
        print("Postorder: ",end="")
        self.postorder()
        print()

    def is_empty(self):
        return self.root is None
    def find_min(self):
        if self.is_empty():
            return None
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.data

    def find_max(self):
        if self.is_empty():
            return None
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.data


def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
  my_bst.traverse()
  print("Max:", my_bst.find_max())
  print("Min:", my_bst.find_min())

main()