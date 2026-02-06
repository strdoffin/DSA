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
    def _find_max(self,node):
        if node is None:
            return None
        curr = node
        while curr.right:
            curr = curr.right
        return curr.data
    def delete(self, data):
        self.root = self._delete(self.root, data)
        if self.root:
            return self.root.data
        return None
    def _delete(self,node, keyd):
        if node is None:
            print("Delete Error, %s is not found in Binary Search Tree."%(keyd))
            return None
        if keyd < node.data:
            node.left = self._delete(node.left, keyd)
        elif keyd > node.data:
            node.right = self._delete(node.right, keyd)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                biggest = self._find_max(node.left)
                node.data = biggest
                node.left = self._delete(node.left, biggest)
        return node

def main():
  my_bst = BST()
  while 1:
    text = input()
    if text == "Done":
      break
    condition, data = text.split(": ")
    if condition == "I":
      my_bst.insert(int(data))
    elif condition == "D":
      my_bst.delete(int(data))
    else:
      print("Invalid Condition")
  my_bst.traverse()

main()